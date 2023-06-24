import RPi.GPIO as GPIO
import time

# Pin definition for controlling the air conditioner
INPUT_PIN = 16

# GPIO setup and mode configuration
def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.OUT)

try:
    # Setup GPIO pin
    setup_gpio()

    while True:
        GPIO.output(INPUT_PIN, 0)
        print("Ceva")
        time.sleep(2)
        GPIO.output(INPUT_PIN, 1)
        print("Altevas")
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
