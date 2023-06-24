import RPi.GPIO as GPIO
from time import sleep

# Pin definitions
INPUT1_PIN = 16
INPUT2_PIN = 18

# GPIO setup and mode configuration
def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT1_PIN, GPIO.OUT)
    GPIO.setup(INPUT2_PIN, GPIO.OUT)

# Control humidity based on the values of humidifier and dehumidifier
def control_humidity(humidity, input1_pin, input2_pin):
    GPIO.output(input1_pin, humidity[0])
    GPIO.output(input2_pin, humidity[1])

try:
    # Setup GPIO pins
    setup_gpio()

    while True:
        control_humidity([0, 1], INPUT1_PIN, INPUT2_PIN)
        print([0, 1][0])
        sleep(2)
        control_humidity([1, 0], INPUT1_PIN, INPUT2_PIN)
        print([1, 0][0])
        sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
