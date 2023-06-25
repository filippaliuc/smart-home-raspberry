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

try: 
    while True:
        pwm.start(0)    
        for x in range(40,100):
            pwm.ChangeDutyCycle(x) 

        GPIO.output(MOTOR_PIN1, GPIO.HIGH)
        GPIO.output(MOTOR_PIN2, GPIO.LOW)

        time.sleep(2)
        pwm.ChangeDutyCycle(0) 
        pwm.stop()
except KeyboardInterrupt:
    GPIO.cleanup()
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
