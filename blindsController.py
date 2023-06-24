from time import sleep 
import RPi.GPIO as GPIO

PWM_PIN=21
CLOCKWISE_PIN=23
ANTI_CLOCKWISE_PIN=19

def blinds_controller(value):

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(CLOCKWISE_PIN, GPIO.OUT)
    GPIO.setup(ANTI_CLOCKWISE_PIN, GPIO.OUT)
    GPIO.setup(PWM_PIN, GPIO.OUT)

    pwm = GPIO.PWM(ENABLE_PIN, 100)  # 100 Hz frequency
    pwm.start(25)

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
    
    pwm.stop()
    GPIO.cleanup()

blinds_controller(1)

