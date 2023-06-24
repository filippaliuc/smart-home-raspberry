import RPi.GPIO as GPIO
import time

def control_air_conditioner(state):
    
    # Definirea pinului GPIO pentru controlul aerului conditionat
    INPUT_PIN = 3

    # Configurarea modului GPIO și a pinilor
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.OUT)

    # Controlul stării pinilor GPIO în funcție de valorile temperaturii
    GPIO.output(INPUT_PIN, state)