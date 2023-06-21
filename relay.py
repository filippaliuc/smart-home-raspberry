import RPi.GPIO as GPIO
from time import sleep

def control_humidity(humidity):
	
	INPUT1_PIN = 16
	INPUT2_PIN = 18
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(INPUT1_PIN, GPIO.OUT)
	GPIO.setup(INPUT2_PIN, GPIO.OUT)

	GPIO.output(INPUT1_PIN, humidity["umidificator"])
	GPIO.output(INPUT2_PIN, humidity["dezumidificator"])


