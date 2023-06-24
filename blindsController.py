import RPi.GPIO as GPIO
from time import sleep

ENABLE_PIN = 21
CLOCKWISE_PIN = 19
ANTI_CLOCKWISE_PIN = 23

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(CLOCKWISE_PIN, GPIO.OUT)
    GPIO.setup(ANTI_CLOCKWISE_PIN, GPIO.OUT)
    GPIO.setup(ENABLE_PIN, GPIO.OUT)

def run():
    setup_gpio()

    pwm = GPIO.PWM(ENABLE_PIN, 100)

    try:
        pwm.start(0)
        GPIO.output(CLOCKWISE_PIN, GPIO.HIGH)
        GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.LOW)

        pwm.ChangeDutyCycle(50)

        GPIO.output(ENABLE_PIN, GPIO.HIGH)

        while True:
            sleep(2)

    except KeyboardInterrupt:
        GPIO.output(ENABLE_PIN, GPIO.LOW)
        pwm.stop()

    finally:
        GPIO.cleanup()

run()
