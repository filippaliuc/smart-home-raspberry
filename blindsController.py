import RPi.GPIO as GPIO
from time import sleep

ENABLE_PIN = 23
CLOCKWISE_PIN = 21
ANTI_CLOCKWISE_PIN = 19

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(CLOCKWISE_PIN, GPIO.OUT)
    GPIO.setup(ANTI_CLOCKWISE_PIN, GPIO.OUT)
    GPIO.setup(ENABLE_PIN, GPIO.OUT)

def run():
    setup_gpio()

    try:
        GPIO.output(ENABLE_PIN, GPIO.HIGH)

        while True:
            GPIO.output(CLOCKWISE_PIN, GPIO.HIGH)
            GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.LOW)
            sleep(2)

            GPIO.output(CLOCKWISE_PIN, GPIO.LOW)
            GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.HIGH)
            sleep(2)

    except KeyboardInterrupt:
        GPIO.output(ENABLE_PIN, GPIO.LOW)

    finally:
        GPIO.cleanup()

run()

