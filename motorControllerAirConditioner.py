import RPi.GPIO as GPIO
import time

inputPin = 35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputPin, GPIO.OUT, initial=GPIO.HIGH)

def motor_on(pin):
    GPIO.output(pin, GPIO.LOW)

def motor_off(pin):
    GPIO.output(pin, GPIO.HIGH)

try:
    motor_on(inputPin)
    print("ON")
    time.sleep(5)
    motor_off(inputPin)
    print("OFF")
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()

