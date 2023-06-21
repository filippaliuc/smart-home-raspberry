import RPi.GPIO as GPIO

DATA_PIN = 36
LATCH_PIN = 38
CLOCK_PIN = 40


def control_led_state(binaryValue):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DATA_PIN,GPIO.OUT)
    GPIO.setup(LATCH_PIN,GPIO.OUT)
    GPIO.setup(CLOCK_PIN,GPIO.OUT)

    GPIO.output(LATCH_PIN, GPIO.LOW)

    for i in range (4):
        GPIO.output(DATA_PIN, int(binaryValue[i-1]))
        GPIO.output(CLOCK_PIN, GPIO.HIGH)
        GPIO.output(CLOCK_PIN, GPIO.LOW)

    GPIO.output(LATCH_PIN, GPIO.HIGH)



