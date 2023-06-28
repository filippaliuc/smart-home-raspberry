from tempAndHumidity import get_temperature_and_humidity
from photoresistor import get_light_state
from distanceSensor import get_distance
from flameSensor import get_flame
from leds import control_led_state
from humidityController import control_humidity
from temperatureController import control_air_conditioner
from buzzer import trigger_fire_alarm
from petFeederController import feed_cat, feed_dog
from blindsController import control_blinds

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
flag = 0

def validate_control_blinds(blinds_state):
    global flag

    if blinds_state and flag:
        control_blinds(blinds_state)
        print("Sa inregistrat ", blinds_state)
        flag = 0
    elif not blinds_state and not flag:
        print("Sa inregistrat ", blinds_state)
        control_blinds(blinds_state)
        flag = 1

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
    # send_photo_thread.join()
    feed_cat_thread.join()
    feed_dog_thread.join()

    # Eliberăm resursele GPIO
    print("error")
    GPIO.cleanup()

def write_log(temperature, is_light, distance, is_flame, alarm, blinds, lights, temperature_controller, humidity_controller):
 
    # Scrie valorile colectate de la senzori cât și starea variabilelor controlerelor
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Deschide fisierul runLog.txt cu opțiunea append, adică adăugare începând de la finalul fișierului
    with open('runLog.txt', 'a') as file:
        file.write('Time: ' + str(current_time) + ':\n')
        file.write('    Temperatură: {0:0.1f} C Umiditate: {1:0.1f} %'.format(temperature, humidity) + ' Lumina ' + str(is_light) + ' Foc ' + str(is_flame) + ' Distanță ' + str(distance) + '\n')
        file.write('    Alarmă: ' + str(alarm) + '\n')
        file.write('    Jaluzele: ' + str(blinds) + '\n')
        file.write('    Lumini: ' + str(lights) + '\n')
        file.write('    Centrală termica: ' + str(temperature_controller["centrala"]) + ', Aer condiționat: ' + str(temperature_controller["clima"]) + '\n')
        file.write('    Umidificator: ' + str(humidity_controller["umidificator"]) + ', Dezumidificator: ' + str(humidity_controller["dezumidificator"]) + '\n')
        file.write('    Calculează predicția: ' + str(database.child("predictie").child("compute").get().val()) + '\n')
        file.write('    Predicție: ' + ('Inactiv' if not database.child("predictie").child("tip").get().val() else database.child("predictie").child("tip").get().val()) + '\n\n')

try:     
    # Începe firul de execuiție al alarmei
    alarm_thread = threading.Thread(target=trigger_fire_alarm)
    alarm_thread.start()

    # Începe firul de execuție al capturii încărcate în Firebase Storage
    # send_photo_thread = threading.Thread(target=upload_capture_to_storage)
    # send_photo_thread.start()

    # Începe firul de execuție al hrănitorului câinelui
    feed_dog_thread = threading.Thread(target=feed_dog)
    feed_dog_thread.start()

    # Începe firul de execuție al hrănitorului pisicii
    feed_cat_thread = threading.Thread(target=feed_cat)
    feed_cat_thread.start()

    while True:
        try:
            # Obținerea informațiilor de la senzori
            temperature, humidity = get_temperature_and_humidity()

            is_light = get_light_state()  
            distance = get_distance()  
            print(distance) 
            is_flame = get_flame()

            # Scrie în baza de date informațiile colectate de la senzori
            write_to_database(temperature, humidity, is_light, distance, is_flame)  

             # Scrie în Cloudwatch informațiile colectate de la senzori
            write_to_cloud(temperature, humidity, is_light, is_flame) 

            # Citește din baza de date valorile variabilelor de stare ale controlerelor diferitelor dispozitive
            alarm, blinds, lights, temperature_controller, humidity_controller = read_from_database()  

            # Scrie în log atât datele colectate de la senzori, cât și valorile variabilelor de stare ale controlerelor citite anterior
            write_log(temperature, is_light, distance, is_flame, alarm, blinds, lights, temperature_controller, humidity_controller) 

            # Transformă starea luminilor într-un șir binar
            binary_string_of_lights = boolean_to_binary(lights=lights)  

            # Controlează starea LED-urilor pe baza valorii binare
            control_led_state(binaryValue=binary_string_of_lights) 
            
            # Controlează aerul condiționat în funcție de temperatura setată
            control_air_conditioner(state=temperature_controller["clima"])  

            # Controlează umiditatea în funcție de umiditatea setată
            control_humidity(humidity=humidity_controller)

            # Controlează jaluzelele
            validate_control_blinds(blinds_state=blinds)
            
        except KeyboardInterrupt:
            break  

except KeyboardInterrupt:
    cleanup()  # Încheierea curățării resurselor în cazul în care se apasă combinația de taste pentru întrerupere


