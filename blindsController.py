import RPi.GPIO as GPIO
import time

def control_blinds(blinds_state):

    ENABLE_PIN = 19
    MOTOR_PIN1 = 21
    MOTOR_PIN2 = 23

    GPIO.setup(ENABLE_PIN, GPIO.OUT)
    GPIO.setup(MOTOR_PIN1, GPIO.OUT)
    GPIO.setup(MOTOR_PIN2, GPIO.OUT)

    pwm = GPIO.PWM(ENABLE_PIN, 100)

    pwm.start(0)
    print("blinds", blinds_state)

    if blinds_state:
            
        # Coboară jaluzelele
        GPIO.output(MOTOR_PIN1, GPIO.HIGH)
        GPIO.output(MOTOR_PIN2, GPIO.LOW)
        

        pwm.ChangeDutyCycle(50)

        time.sleep(2)
    elif not blinds_state:

        # Ridică jaluzelele
        GPIO.output(MOTOR_PIN1, GPIO.LOW)
        GPIO.output(MOTOR_PIN2, GPIO.HIGH)

        pwm.ChangeDutyCycle(50)

        time.sleep(2)

    pwm.stop()