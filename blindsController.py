# from time import sleep 
# import RPi.GPIO as GPIO

# ENABLE_PIN=21
# CLOCKWISE_PIN=23
# ANTI_CLOCKWISE_PIN=19

# def blinds_controller(value):

#     GPIO.setmode(GPIO.BOARD)

#     GPIO.setup(CLOCKWISE_PIN, GPIO.OUT)
#     GPIO.setup(ANTI_CLOCKWISE_PIN, GPIO.OUT)
#     GPIO.setup(ENABLE_PIN, GPIO.OUT)

#     pwm = GPIO.PWM(ENABLE_PIN, 100)  # 100 Hz frequency
#     pwm.start(50)

#     if value:
#         GPIO.output(CLOCKWISE_PIN, GPIO.HIGH)
#         GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.LOW)
#         sleep(4)
#         GPIO.output(CLOCKWISE_PIN, GPIO.LOW)
#     else: 
#         GPIO.output(CLOCKWISE_PIN, GPIO.LOW)
#         GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.HIGH)
#         sleep(4)
#         GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.LOW)
    
#     pwm.stop()
#     GPIO.cleanup()

# blinds_controller(1)

# from time import sleep
# from gpiozero import Motor, LED

# ENABLE_PIN=9
# CLOCKWISE_PIN=10
# ANTI_CLOCKWISE_PIN=11

# motor = Motor(ANTI_CLOCKWISE_PIN, CLOCKWISE_PIN)
# motorSwitch = LED(ENABLE_PIN)

# motorSpeedForward = 1

# def run():
#     motorSwitch.on()
#     sleep(2)
#     motor.forward(speed=0.9)
#     sleep(5)
#     motor.backward(speed=0.9)
#     sleep(5)
#     motorSwitch.off()

# run()

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

ENABLE_PIN=21
CLOCKWISE_PIN=19
ANTI_CLOCKWISE_PIN=23

GPIO.setup(CLOCKWISE_PIN, GPIO.OUT)
GPIO.setup(ANTI_CLOCKWISE_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)


def run():
    pwm=GPIO.PWM(ENABLE_PIN, 100)

    pwm.start(0)
    GPIO.output(CLOCKWISE_PIN, GPIO.HIGH)
    GPIO.output(ANTI_CLOCKWISE_PIN, GPIO.LOW)

    pwm.ChangeDutyCycle(50)

    GPIO.output(ENABLE_PIN, GPIO.HIGH)

    sleep(2)

    GPIO.output(ENABLE_PIN, GPIO.LOW)

    pwm.stop()

    GPIO.cleanup()