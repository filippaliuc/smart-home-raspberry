import RPi.GPIO as GPIO
from time import sleep

# Define GPIO pins for Motor Driver Inputs
Motor1A = 19
Motor1B = 21
Motor1E = 23

def setup():
    GPIO.setmode(GPIO.BOARD)        # GPIO numbering mode
    GPIO.setup(Motor1A, GPIO.OUT)   # Set pin as output
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

def loop():
    # Going forwards
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    sleep(5)

    # Going backwards
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    sleep(5)

    # Stop
    GPIO.output(Motor1E, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        cleanup()
