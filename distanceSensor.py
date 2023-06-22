import RPi.GPIO as GPIO
import time

# Definirea pinilor GPIO pentru senzorul de distanță ultrasunete
HCSR40_TRIGGER = 29
HCSR40_ECHO = 31

def ping_distance_sensor():
    # Setează pinul trigger la nivel scăzut (LOW)
    GPIO.output(HCSR40_TRIGGER, GPIO.LOW)

    # Așteaptă ca senzorul să se stabilizeze
    time.sleep(2)

    # Trezește senzorul
    GPIO.output(HCSR40_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(HCSR40_TRIGGER, GPIO.LOW)


def get_distance():
    # Setează modul GPIO și configurările pinilor
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(HCSR40_TRIGGER, GPIO.OUT)
    GPIO.setup(HCSR40_ECHO, GPIO.IN)

    # Trezește senzorul și îl stabilizează a senzorului de distanță
    ping_distance_sensor()

    # Măsoară timpul necesar întoarcerii semnalului de ecou
    while GPIO.input(HCSR40_ECHO) == 0:
        pulse_start_time = time.time()

    while GPIO.input(HCSR40_ECHO) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    # Calculează distanța utilizând viteza sunetului
    distance = round(pulse_duration * 17150, 2)

    return distance
