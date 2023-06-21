import RPi.GPIO as GPIO

def get_flame():
	FLAME_SENSOR = 37

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(FLAME_SENSOR,GPIO. IN)
	
	is_flame = GPIO.input(FLAME_SENSOR)
	
	return is_flame
