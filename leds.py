import RPi.GPIO as GPIO

# Definirea pinilor GPIO pentru registrul care controlează luminile
DATA_PIN = 36
LATCH_PIN = 38
CLOCK_PIN = 40

def control_led_state(binaryValue):
    # Setarea modului GPIO și configurarea pinilor pentru LED-uri
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DATA_PIN, GPIO.OUT)
    GPIO.setup(LATCH_PIN, GPIO.OUT)
    GPIO.setup(CLOCK_PIN, GPIO.OUT)

    # Setarea pinul LATCH la nivel scăzut (LOW) pentru a începe transmiterea valorii binare.
    GPIO.output(LATCH_PIN, GPIO.LOW)

    # Parcurgerea celor 4 biți ai valorii binare și actualizăm pinul DATA în funcție de fiecare bit.
    for i in range(4):
        # Setarea pinului DATA în funcție de valoarea binară
        GPIO.output(DATA_PIN, int(binaryValue[i-1]))
        
        # Setarea pinul CLOCK la nivel înalt (HIGH) și apoi la nivel scăzut (LOW) pentru a sincroniza transmiterea bitului.
        GPIO.output(CLOCK_PIN, GPIO.HIGH)
        GPIO.output(CLOCK_PIN, GPIO.LOW)

    # Setarea pinul LATCH la nivel înalt (HIGH) pentru a actualiza starea LED-urilor.
    GPIO.output(LATCH_PIN, GPIO.HIGH)
