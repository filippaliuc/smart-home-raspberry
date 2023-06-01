# blink.py

import time 
import RPi.GPIO as GPIO

led_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.output(led_pin,True)
time.sleep(1)
GPIO.output(led_pin,False)

GPIO.cleanup()
