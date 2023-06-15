from tempAndHumidity import getHumidityAndTemperature
from photoresistor import getLightIntensity
from distanceSensor import getDistance
from flameSensor import getFlame
from leds import controlLedState
from buzzer import triggerFireAlarm
from firebase import database

import RPi.GPIO as GPIO
import time
import threading

GPIO.setwarnings(False)

def writeDataToFirebase():
    temperature, humidity = getHumidityAndTemperature()
    isLight = getLightIntensity()
    distance = getDistance()
    flame = getFlame()
    
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



try: 

    stop_event = threading.Event()
    thread = threading.Thread(target=triggerFireAlarm)  
    while True:
        # writeDataToFirebase()
        alarm, blinds, lights, temperature, humidity = readDataFromFirebase()
        binary_string_of_lights = booleanToBinary(lights=lights)
        print(type(binary_string_of_lights))
        
        controlLedState(binaryValue=binary_string_of_lights)

        is_flame = getFlame()
        if(not thread.is_alive()):
            if(is_flame == 1):
                thread.start()
            else: 
                stop_event.set()
      
        
        time.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nDone")
