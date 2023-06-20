import RPi.GPIO as GPIO
from firebase import database

def getLightIntensity():

    LIGHT_SENSOR = 15
    LED_PIN = 37

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT_SENSOR,GPIO.IN)
    GPIO.setup(LED_PIN,GPIO.OUT)

    isLight = GPIO.input(LIGHT_SENSOR)

    if(isLight):
        print("lumina 1")
        GPIO.output(LED_PIN,GPIO.LOW)
    else:
        print("lumina 0")
        GPIO.output(LED_PIN,GPIO.HIGH)

    GPIO.cleanup()
    
    return isLight
    
