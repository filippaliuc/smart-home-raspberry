from tempAndHumidity import get_temperature_and_humidity
from photoresistor import get_light_state
from distanceSensor import get_distance
from flameSensor import get_flame
from leds import control_led_state
from humidityController import control_humidity
from temperatureController import control_air_conditioner
from buzzer import trigger_fire_alarm
from petFeederController import feed_cat, feed_dog

from firebase import database, storage
from cloudwatchService import cloudwatch

import RPi.GPIO as GPIO
from picamera import PiCamera

import time
import threading
import os
import datetime

GPIO.setwarnings(False)

distance = 0


def write_to_database(temperature, humidity, isLight, distance, flame):
    # Definește un dicționar pentru datele pe care dorim să le scriem în baza de date
    data = {
        "temperatura(C)": temperature,
        "umiditate(%)": humidity,
        "lumina": isLight,
        "distanta(cm)": distance,
        "foc": flame
    }

    # Scrie datele în nodul "semnale" din baza de date
    database.child("semnale").set(data)


def read_from_database():
    # Citește valorile din nodul "control" din baza de date
    controls = database.child("control").get()
    
    # Returnează valorile specifice pentru alarma, jaluzele, lumini, temperatura și umiditate
    return controls.val()["alarma"], controls.val()["jaluzele"], controls.val()["lumini"], controls.val()["temperatura"], controls.val()["umiditate"]


def boolean_to_binary(lights):
    
    # Convertește valorile de stare a luminilor din format boolean în format binar de tip șir de caractere
    binary_value = int(lights["baie"]) * 8 + int(lights["bucatarie"]) * 4 + int(lights["dormitor"]) * 2 + int(lights["lampa"]) * 1
    binary_string = format(binary_value, '04b')
    return binary_string

def write_to_cloud(temperature, humidity, isLight, flame): 
    
    # Definește un spațiu de nume pentru metricile care vor fi înregistrate în serviciul CloudWatch
    namespace = 'HOME_AUTOMATION_METRICS'

    # Înregistrează metrica pentru temperatură în CloudWatch
    cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName' : 'Temperatura Celsius',
                'Unit' : 'None',
                'Value' : temperature
            },
        ],
        Namespace=namespace
    )

    # Înregistrează metrica pentru umiditate în CloudWatch
    cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName' : 'Umiditate',
                'Unit' : 'None',
                'Value' : humidity
            },
        ],
        Namespace=namespace
    )   

    cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName' : 'Lumina',
                'Unit' : 'None',
                'Value' : isLight
            },
        ],
        Namespace=namespace
    )   

    cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName' : 'Foc',
                'Unit' : 'None',
                'Value' : flame
            },
        ],
        Namespace=namespace
    )   

def  upload_capture_to_storage():
    while True:
        # Setează valoarea nodului "compute" din nodul "predictie" în baza de date la 0
        database.child("predictie").child("compute").set(0)
        
        # Verifică distanța față de hrănitor
        if distance < 20 and distance > 15:

            # Setăm valoarea nodului "compute" din nodul "predictie" în baza de date la 1
            database.child("predictie").child("compute").set(1)

            destination_path = 'model/pet_image.jpeg'
            image_path = "capture.jpeg"

            # Inițializăm camera Raspberry Pi
            camera = PiCamera()

            time.sleep(2)

            # Capturăm imaginea
            camera.capture(image_path)
            print("captured", datetime.datetime.now())

            # Închidem camera
            camera.close()

            # Încărcăm imaginea în firebase storage
            storage.child(destination_path).put(image_path)
            os.remove(image_path)

            time.sleep(2)

def cleanup():

    # Așteptăm încheierea firelor de execuție pentru alarmă, încărcare imagine și hrănirea animalelor de companie
    alarm_thread.join()
    send_photo_thread.join()
    feed_cat_thread.join()
    feed_dog_thread.join()

    # Eliberăm resursele GPIO
    GPIO.cleanup()

def write_log(temperature, is_light, distance, is_flame, alarm, blinds, lights, temperature_controller, humidity_controller):

    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open('runLog.txt', 'a') as file:
        file.write('Time: ' + str(current_time) + ':\n')
        file.write('    Temperatură: {0:0.1f} C Umiditate: {1:0.1f} %'.format(temperature, humidity) + ' Lumina ' + str(is_light) + ' Foc ' + str(is_flame) + ' Distanță ' + str(distance) + '\n')
        file.write('    Alarmă: ' + str(1 if not is_flame else 0) + '\n')
        file.write('    Jaluzele: ' + str(blinds) + '\n')
        file.write('    Lumini: ' + str(lights) + '\n')
        file.write('    Centrală termica: ' + str(temperature_controller["centrala"]) + ', Aer condiționat: ' + str(temperature_controller["clima"]) + '\n')
        file.write('    Umidificator: ' + str(humidity_controller["umidificator"]) + ', Dezumidificator: ' + str(humidity_controller["dezumidificator"]) + '\n')
        file.write('    Calculează predicția: ' + str(database.child("predictie").child("compute").get().val()) + '\n')
        file.write('    Predicție: ' + ('Inactiv' if not database.child("predictie").child("tip").get().val() else database.child("predictie").child("tip").get().val()) + '\n\n')



try: 
    alarm_thread = threading.Thread(target=trigger_fire_alarm)
    alarm_thread.start()

    send_photo_thread = threading.Thread(target=upload_capture_to_storage)
    send_photo_thread.start()

    feed_dog_thread = threading.Thread(target=feed_dog)
    feed_dog_thread.start()

    feed_cat_thread = threading.Thread(target=feed_cat)
    feed_cat_thread.start()

    while True:
        try:
            temperature, humidity = get_temperature_and_humidity()
            is_light = get_light_state()
            distance = get_distance()
            is_flame = get_flame()

            write_to_database(temperature, humidity, is_light, distance, is_flame)
            write_to_cloud(temperature, humidity, is_light, is_flame)

            alarm, blinds, lights, temperature_controller, humidity_controller = read_from_database()

            write_log(temperature, is_light, distance, is_flame, alarm, blinds, lights, temperature_controller, humidity_controller)

            binary_string_of_lights = boolean_to_binary(lights=lights)
            control_led_state(binaryValue=binary_string_of_lights)

            control_air_conditioner(temperature=temperature_controller)

            control_humidity(humidity=humidity_controller)


            time.sleep(0.0005)

        except KeyboardInterrupt:
            break



except KeyboardInterrupt:
    cleanup()

