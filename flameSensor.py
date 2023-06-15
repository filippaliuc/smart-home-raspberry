import RPi.GPIO as GPIO

def getFlame():
	FLAME_SENSOR = 37

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(FLAME_SENSOR,GPIO. IN)
	
	isFlame = GPIO.input(FLAME_SENSOR)

	GPIO.cleanup()
	
	return isFlame
