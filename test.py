import RPi.GPIO as GPIO
import time

def control_blinds():

    ENABLE_PIN = 19
    MOTOR_PIN1 = 21
    MOTOR_PIN2 = 23

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ENABLE_PIN, GPIO.OUT)
    GPIO.setup(MOTOR_PIN1, GPIO.OUT)
    GPIO.setup(MOTOR_PIN2, GPIO.OUT)

    GPIO.output(ENABLE_PIN, GPIO.HIGH)

    GPIO.output(MOTOR_PIN1, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(MOTOR_PIN1, GPIO.LOW)

    GPIO.output(ENABLE_PIN, GPIO.LOW)
    
    GPIO.cleanup()


control_blinds()
# time.sleep(4)
# control_blinds(1)
