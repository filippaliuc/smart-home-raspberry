import RPi.GPIO as GPIO
from time import sleep

dataPin = 36
latchPin = 38
clockPin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(dataPin,GPIO.OUT)
GPIO.setup(latchPin,GPIO.OUT)
GPIO.setup(clockPin,GPIO.OUT)

def changeLedState(binaryValue):

    # GPIO.output(clockPin, GPIO.LOW)
    # GPIO.output(latchPin, GPIO.LOW)
    # GPIO.output(clockPin, GPIO.HIGH)

    for _ in range (8):
        GPIO.output(dataPin, (binaryValue >> 7) & 1)
        GPIO.output(clockPin, GPIO.HIGH)
        GPIO.output(clockPin, GPIO.LOW)
        binaryValue <<= 1

    GPIO.output(clockPin, GPIO.LOW)
    GPIO.output(latchPin, GPIO.HIGH)
    GPIO.output(latchPin, GPIO.LOW)
    GPIO.output(clockPin, GPIO.HIGH)


changeLedState(0b0000)

GPIO.cleanup()
