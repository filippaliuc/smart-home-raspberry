import RPi.GPIO as GPIO
from time import sleep

def control_humidity(humidity):
    # Definirea pinilor GPIO pentru umidificator și dezumidificator
    INPUT1_PIN = 16
    INPUT2_PIN = 18
    
    # Configurarea modului GPIO și a pinilor
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT1_PIN, GPIO.OUT)
    GPIO.setup(INPUT2_PIN, GPIO.OUT)
    
    # Controlul stării pinilor GPIO în funcție de valorile umidificatorului și dezumidificatorului
    GPIO.output(INPUT1_PIN, humidity[0])
    GPIO.output(INPUT2_PIN, humidity[1])
    GPIO.cleanup()


try:
    while True:
        control_humidity([0,1])
        sleep(2)
        control_humidity([1,0])

except KeyboardInterrupt
    GPIO.cleanup()