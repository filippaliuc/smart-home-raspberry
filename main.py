from tempAndHumidity import get_temperature_and_humidity
from photoresistor import get_light_state
from distanceSensor import get_distance
from flameSensor import get_flame
from leds import control_led_state
from firebase import database, storage
from humidityController import control_humidity
from temperatureController import control_air_conditioner
from cloudwatchService import cloudwatch
from buzzer import trigger_fire_alarm
from picamera import PiCamera

import RPi.GPIO as GPIO
import time
import threading
import os
import datetime

GPIO.setwarnings(False)

distance = 0


def write_to_database(temperature, humidity, isLight, distance, flame):

    data = {
        "temperatura(C)":temperature,
        "umiditate(%)":humidity,
        "lumina":isLight,
        "distanta(cm)":distance,
        "foc":flame
    }

    database.child("semnale").set(data) 

def read_from_database():
    controls = database.child("control").get()
    return controls.val()["alarma"], controls.val()["jaluzele"], controls.val()["lumini"], controls.val()["temperatura"], controls.val()["umiditate"]

def boolean_to_binary(lights):
    binary_value = int(lights["baie"]) * 8 + int(lights["bucatarie"]) * 4 + int(lights["dormitor"]) * 2 + int(lights["lampa"]) * 1
    binary_string = format(binary_value, '04b')
    return binary_string

def write_to_cloud(temperature, humidity, isLight, flame): 
    
    namespace = 'HOME_AUTOMATION_METRICS'

    # Put metrics
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
        database.child("predictie").child("compute").set(0)
        if distance < 20 and distance > 15:
            database.child("predictie").child("compute").set(1)

            destination_path = 'model/pet_image.jpeg'
            image_path = ("capture.jpeg")

            camera = PiCamera()

            time.sleep(2)

            camera.capture(image_path)
            print("captured", datetime.datetime.now())

            camera.close()

            storage.child(destination_path).put(image_path)
            os.remove(image_path)

            time.sleep(2)
    
def cleanup():
    alarm_thread.join()
    send_photo_thread.join()
    GPIO.cleanup()
    print("\nDone")

try: 
    alarm_thread = threading.Thread(target=trigger_fire_alarm)
    alarm_thread.start()

    send_photo_thread = threading.Thread(target=upload_capture_to_storage)
    send_photo_thread.start()

    while True:
        try:
            temperature, humidity = get_temperature_and_humidity()
            is_light = get_light_state()
            distance = get_distance()
            is_flame = get_flame()

            print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature,humidity),'Lumina ', is_light, ' Foc ', is_flame, ' Distanta ', distance)

            write_to_database(temperature, humidity, is_light, distance, is_flame)
            write_to_cloud(temperature, humidity, is_light, is_flame)

            alarm, blinds, lights, temperature_controller, humidity_controller = read_from_database()

            binary_string_of_lights = boolean_to_binary(lights=lights)
            control_led_state(binaryValue=binary_string_of_lights)

            control_air_conditioner(temperature=temperature_controller)

            control_humidity(humidity=humidity_controller)


            time.sleep(0.0005)

        except KeyboardInterrupt:
            break



except KeyboardInterrupt:
    cleanup()

