import RPi.GPIO as GPIO
import math
from time import sleep	
from flameSensor import get_flame

def trigger_fire_alarm():

	BUZZER_PIN = 22
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BUZZER_PIN, GPIO.OUT)

	global PWM
	PWM = GPIO.PWM(BUZZER_PIN, 1)
	PWM.start(0)
	
	while True: 
		is_flame = get_flame()
		if not is_flame:
			PWM.start(50)
			for x in range (0, 361):
				sin_val = math.sin(x*(math.pi/180))
				tone_val = 2000 + sin_val*500
				PWM.ChangeFrequency(tone_val)
				sleep(0.001)
		else: 
			PWM.stop()
