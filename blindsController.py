import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ENABLE_PIN = 32
MOTOR_PIN1 = 21
MOTOR_PIN2 = 19

GPIO.setup(ENABLE_PIN, GPIO.OUT)
GPIO.setup(MOTOR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_PIN2, GPIO.OUT)

# pwm = GPIO.PWM(ENABLE_PIN, 100)
# try: 
#     while True:
#         pwm.start(0)

#         # Rotate clockwise
#         GPIO.output(MOTOR_PIN1, GPIO.HIGH)
#         GPIO.output(MOTOR_PIN2, GPIO.LOW)

#         for dc in range(0, 101, 5):
#             pwm.ChangeDutyCycle(dc)
#             time.sleep(0.1)

#         time.sleep(2)

#         # Rotate counterclockwise
#         GPIO.output(MOTOR_PIN1, GPIO.LOW)
#         GPIO.output(MOTOR_PIN2, GPIO.HIGH)

#         for dc in range(100, -1, -5):
#             pwm.ChangeDutyCycle(dc)
#             time.sleep(0.1)

#         time.sleep(2)
# except KeyboardInterrupt:
#     GPIO.cleanup()
#     pwm.stop()
print("FW")

GPIO.output(ENABLE_PIN, GPIO.HIGH)
GPIO.output(MOTOR_PIN1, GPIO.HIGH)
GPIO.output(MOTOR_PIN2, GPIO.LOW)

time.sleep(4)

print("BW")

GPIO.output(MOTOR_PIN2, GPIO.HIGH)
GPIO.output(MOTOR_PIN1, GPIO.LOW)


time.sleep(4)

print("stop")

GPIO.output(ENABLE_PIN, GPIO.LOW)

GPIO.cleanup()
