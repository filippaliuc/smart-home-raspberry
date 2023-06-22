import RPi.GPIO as GPIO
import time

def control_air_conditioner(temperature):

    INPUT_PIN = 32

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.OUT)

    GPIO.output(INPUT_PIN, temperature["clima"])
        

