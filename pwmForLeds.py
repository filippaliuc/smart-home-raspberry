#pwmForLeds.py

import time
import RPi.GPIO as GPIO

led_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
pwm = GPIO.PWM(led_pin,100)
pwm.start(0)

try: 
    while 1: 
        for x in range (100):
            pwm.ChangeDutyCycle(x)
            time.sleep(0.01)
        
        for x in range (100,0,-1):
            pwm.ChangeDutyCycle(x)
            time.sleep(0.01)
except KeyboardInterrupt:
    print("Loop ended")

pwm.stop()
GPIO.cleanup()
