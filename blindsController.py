import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ENABLE_PIN = 32
MOTOR_PIN1 = 21
MOTOR_PIN2 = 19

GPIO.setup(ENABLE_PIN, GPIO.OUT)
GPIO.setup(MOTOR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_PIN2, GPIO.OUT)

pwm = GPIO.PWM(ENABLE_PIN, 50)
pwm.start(0)
try: 
    while True:
        pwm.start(50)    
        for x in range(40,100):
            pwm.ChangeFrequency(x) 
            pwm.ChangeDutyCycle(x)
            time.sleep(0.1)
            GPIO.output(ENABLE_PIN, GPIO.HIGH)
            GPIO.output(MOTOR_PIN1, GPIO.HIGH)
            GPIO.output(MOTOR_PIN2, GPIO.HIGH)

        time.sleep(0.01)
        GPIO.output(ENABLE_PIN, GPIO.LOW)
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
