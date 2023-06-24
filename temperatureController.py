import RPi.GPIO as GPIO
import time

def control_air_conditioner(state):
    # Definirea pinului GPIO pentru controlul aerului condiționat
    INPUT_PIN = 32
    print(temperature)
    # Configurarea modului GPIO și a pinului pentru controlul aerului condiționat
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.OUT)
    
    GPIO.output(INPUT_PIN, state)
    # GPIO.cleanup()

control_air_conditioner(1)
