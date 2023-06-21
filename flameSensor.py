import RPi.GPIO as GPIO
import time

def getFlame():
	FLAME_SENSOR = 37

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(FLAME_SENSOR,GPIO. IN)
	
	isFlame = GPIO.input(FLAME_SENSOR)
	# print("foc", isFlame)
	
	# GPIO.cleanup()
	
	return isFlame

# while True: 
# 	print("foc", getFlame())
# 	time.sleep(1)
