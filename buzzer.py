import RPi.GPIO as GPIO
import math
from time import sleep	
from flameSensor import getFlame

def triggerFireAlarm():

	BUZZER_PIN = 22
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BUZZER_PIN, GPIO.OUT)

	global PWM
	PWM = GPIO.PWM(BUZZER_PIN, 1)
	PWM.start(0)
	
	while True: 
		is_flame = getFlame()
		if not is_flame:
			PWM.start(50)
			for x in range (0, 361):
				sinVal = math.sin(x*(math.pi/180))
				toneVal = 2000 + sinVal*500
				PWM.ChangeFrequency(toneVal)
				sleep(0.001)
				# print("On")
		else: 
			PWM.stop()
			# print("Off")
