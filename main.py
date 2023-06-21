from tempAndHumidity import getHumidityAndTemperature
from photoresistor import getLightIntensity
from distanceSensor import getDistance
from flameSensor import getFlame
from leds import controlLedState
from firebase import database, storage
from relay import controlHumidity
from cloudwatchService import cloudwatch
from buzzer import triggerFireAlarm
from picamera import PiCamera

import RPi.GPIO as GPIO
import time
import threading
import os
import datetime

GPIO.setwarnings(False)

distance = 0


def writeDataToFirebase(temperature, humidity, isLight, distance, flame):

    data = {
        "temperatura(C)":temperature,
        "umiditate(%)":humidity,
        "lumina":isLight,
        "distanta(cm)":distance,
        "foc":flame
    }

    database.child("semnale").set(data) 
    # print(data)

def readDataFromFirebase():
    controls = database.child("control").get()
    return controls.val()["alarma"], controls.val()["jaluzele"], controls.val()["lumini"], controls.val()["temperatura"], controls.val()["umiditate"]

def booleanToBinary(lights):
    binary_value = int(lights["baie"]) * 8 + int(lights["bucatarie"]) * 4 + int(lights["dormitor"]) * 2 + int(lights["lampa"]) * 1
    binary_string = format(binary_value, '04b')
    print(binary_string)
    return binary_string

def writeToAWSCloud(temperature, humidity, isLight, flame): 
    
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
            print("captured")

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
    alarm_thread = threading.Thread(target=triggerFireAlarm)
    alarm_thread.start()

    send_photo_thread = threading.Thread(target=upload_capture_to_storage)
    send_photo_thread.start()

    while True:
        try:
            temperature, humidity = getHumidityAndTemperature()
            isLight = getLightIntensity()
            distance = getDistance()
            is_flame = getFlame()

            print(distance)
            writeDataToFirebase(temperature, humidity, isLight, distance, is_flame)
            writeToAWSCloud(temperature, humidity, isLight, is_flame)
            alarm, blinds, lights, temperature, humidity = readDataFromFirebase()

            binary_string_of_lights = booleanToBinary(lights=lights)
            controlLedState(binaryValue=binary_string_of_lights)

            controlHumidity(humidity=humidity)

            time.sleep(0.0005)

        except KeyboardInterrupt:
            # Perform any necessary cleanup or logging here
            break



except KeyboardInterrupt:
    cleanup()

