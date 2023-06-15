import RPi.GPIO as GPIO
from time import sleep

dataPin = 36
latchPin = 38
clockPin = 40


def controlLedState(binaryValue):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin,GPIO.OUT)
    GPIO.setup(latchPin,GPIO.OUT)
    GPIO.setup(clockPin,GPIO.OUT)

    GPIO.output(latchPin, GPIO.LOW)

    for i in range (4):
        GPIO.output(dataPin, int(binaryValue[i-1]))
        GPIO.output(clockPin, GPIO.HIGH)
        GPIO.output(clockPin, GPIO.LOW)

    GPIO.output(latchPin, GPIO.HIGH)

    # GPIO.cleanup()


