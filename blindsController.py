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

from time import sleep
from guizero import App, Text, PushButton
from gpiozero import Motor, LED

ENABLE_PIN=9
CLOCKWISE_PIN=10
ANTI_CLOCKWISE_PIN=11

motor = Motor(CLOCKWISE_PIN, ANTI_CLOCKWISE_PIN)
motorSwitch = LED(ENABLE_PIN)

app = App(title="GUI Development", layout="grid", height=600, width=800)
message = Text(app, text="Single Motor Control Interface", grid=[4,0])

motorSpeedForward = 0.5
motorSpeedBackward = 0.5


def run():
    motorSwitch.on()
    motor.forward(speed=motorSpeedForward)
    sleep(5)
    motor.backward(speed=motorSpeedBackward)
    sleep(5)
    motorSwitch.off()
    
run()