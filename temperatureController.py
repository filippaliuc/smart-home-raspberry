import RPi.GPIO as GPIO
import time

def control_air_conditioner(temperature):
    # Definirea pinului GPIO pentru controlul aerului condiționat
    INPUT_PIN = 32

    # Configurarea modului GPIO și a pinului pentru controlul aerului condiționat
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.OUT)

    # Controlul stării pinului GPIO în funcție de valoarea temperaturii
    print(temperature["clima"])
    if temperature["clima"]:
        GPIO.output(INPUT_PIN, GPIO.LOW)
    else: 
        GPIO.output(INPUT_PIN, GPIO.HIGH)