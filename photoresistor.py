import RPi.GPIO as GPIO
from firebase import database

GPIO.setmode(GPIO.BOARD)

LIGHT_SENSOR = 15
LED_PIN = 37

GPIO.setup(LIGHT_SENSOR,GPIO.IN)
GPIO.setup(LED_PIN,GPIO.OUT)

def getLightIntensity():

    isLight = GPIO.input(LIGHT_SENSOR)

    print("E lumina: ",isLight)
    # database.child("semnale").child("lumina").set(isLight)

    if(not isLight):
        GPIO.output(LED_PIN,GPIO.LOW)
    else:
        GPIO.output(LED_PIN,GPIO.HIGH)

    return isLight
    
