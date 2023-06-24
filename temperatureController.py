import RPi.GPIO as GPIO
import time

    
    # Definirea pinului GPIO pentru controlul aerului conditionat
INPUT_PIN = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN, GPIO.OUT)


try:
    while True: 
        GPIO.output(INPUT_PIN, 0)
        time.sleep(2)
        GPIO.output(INPUT_PIN, 1)
except KeyboardInterrupt:
    GPIO.cleanup()