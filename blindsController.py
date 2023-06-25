import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ENABLE_PIN = 32
MOTOR_PIN1 = 21
MOTOR_PIN2 = 23

GPIO.setup(ENABLE_PIN, GPIO.OUT)
GPIO.setup(MOTOR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_PIN2, GPIO.OUT)

pwm = GPIO.PWM(ENABLE_PIN, 100)

while True:
    pwm.start(0)    
    for x in range(40,100):
        pwm.ChangeDutyCycle(50) 

    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.HIGH)

    pwm.stop()
    time.sleep(2)

# print("FW")

# GPIO.output(ENABLE_PIN, GPIO.HIGH)
# GPIO.output(MOTOR_PIN1, GPIO.HIGH)
# GPIO.output(MOTOR_PIN2, GPIO.LOW)

# time.sleep(4)

# print("BW")

# GPIO.output(MOTOR_PIN2, GPIO.HIGH)
# GPIO.output(MOTOR_PIN1, GPIO.LOW)


# time.sleep(4)

# print("stop")

# GPIO.output(ENABLE_PIN, GPIO.LOW)

# GPIO.cleanup()
