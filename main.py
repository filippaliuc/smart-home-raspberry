from tempAndHumidity import getHumidityAndTemperature
from photoresistor import getLightIntensity
from distanceSensor import getDistance
from flameSensor import getFlame
from leds import controlLedState
from firebase import database
from relay import controlHumidity
from cloudwatchService import cloudwatch

import RPi.GPIO as GPIO
import time
import threading

GPIO.setwarnings(False)

alarm_active = threading.Event()


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



         
try: 

    while True:
        temperature, humidity = getHumidityAndTemperature()
        isLight = getLightIntensity()
        distance = getDistance()
        flame = getFlame()

        writeDataToFirebase(temperature, humidity, isLight, distance, flame)
        writeToAWSCloud(temperature, humidity, isLight, flame)
        alarm, blinds, lights, temperature, humidity = readDataFromFirebase()
        
        # binary_string_of_lights = booleanToBinary(lights=lights)
        # controlLedState(binaryValue=binary_string_of_lights)

        # controlHumidity(humidity=humidity)
        
        
        time.sleep(0.5)


except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nDone")
