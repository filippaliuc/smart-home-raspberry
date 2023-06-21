import RPi.GPIO as GPIO
import time

HCSR40_TRIGGER = 29
HCSR40_ECHO = 31

def ping_distance_sensor():

    GPIO.output(HCSR40_TRIGGER, GPIO.LOW)

    # print("Waiting for sensor to settle")

    time.sleep(2)

    # print("Calculating distance")

    GPIO.output(HCSR40_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(HCSR40_TRIGGER, GPIO.LOW)


def get_distance():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(HCSR40_TRIGGER, GPIO.OUT)
    GPIO.setup(HCSR40_ECHO, GPIO.IN)

    ping_distance_sensor()

    while GPIO.input(HCSR40_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(HCSR40_ECHO)==1:
        pulse_end_time=time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    distance = round(pulse_duration * 17150, 2)
    
    return distance

