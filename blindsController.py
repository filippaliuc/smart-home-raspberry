from machine import Pin, PWM
from time import sleep 
from RPi.GPIO import GPIO

PWM_PIN=21
CLOCKWISE_PIN=23
ANTI_CLOCKWISE_PIN=19

def blinds_controller(value):

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(CLOCKWISE_PIN, GPIO.OUT)
    GPIO.setup(ANTI_CLOCKWISE_PIN, GPIO.OUT)
    Speed = PWM(GPIO.setup(PWM_PIN, GPIO.OUT))


    Speed.freq(50)
    speed = 50

    Speed.duty_u16(int(speed/100*65536))

    if value:
        GPIO.output(CLOCKWISE_PIN, GPIO.HIGH)
        GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.LOW)
        sleep(2)
        GPIO.output(CLOCKWISE_PIN, GPIO.LOW)
    else: 
        GPIO.output(CLOCKWISE_PIN, GPIO.LOW)
        GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.HIGH)
        sleep(2)
        GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.LOW)

blinds_controller(1)

