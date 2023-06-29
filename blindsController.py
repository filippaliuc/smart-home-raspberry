import RPi.GPIO as GPIO
import time

def control_blinds(blinds_state):

    ENABLE_PIN = 19
    MOTOR_PIN1 = 21
    MOTOR_PIN2 = 23

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ENABLE_PIN, GPIO.OUT)
    GPIO.setup(MOTOR_PIN1, GPIO.OUT)
    GPIO.setup(MOTOR_PIN2, GPIO.OUT)

    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)

    GPIO.output(ENABLE_PIN, GPIO.HIGH)

    pwm = GPIO.PWM(ENABLE_PIN, 100)

    pwm.start(50)

    # Go down
    if blinds_state:
            
        # Coboară jaluzelele
        GPIO.output(MOTOR_PIN1, GPIO.LOW)
        GPIO.output(MOTOR_PIN2, GPIO.HIGH)
        

        pwm.ChangeDutyCycle(50)

        time.sleep(2)

        GPIO.output(MOTOR_PIN1, GPIO.LOW)

    # Go up
    elif not blinds_state:

        # Ridică jaluzelele
        GPIO.output(MOTOR_PIN1, GPIO.HIGH)
        GPIO.output(MOTOR_PIN2, GPIO.LOW)

        pwm.ChangeDutyCycle(60)

        time.sleep(1.5)

        GPIO.output(MOTOR_PIN2, GPIO.LOW)


    pwm.stop()
    GPIO.output(ENABLE_PIN, GPIO.LOW)
    # GPIO.cleanup()