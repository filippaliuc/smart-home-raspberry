import RPi.GPIO as GPIO
from time import sleep

def controlHumidity(humidity):
	
	input1Pin = 16
	input2Pin = 18
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(input1Pin, GPIO.OUT)
	GPIO.setup(input2Pin, GPIO.OUT)

	print("ceva")

	GPIO.output(input1Pin, humidity["umidificator"])
	GPIO.output(input2Pin, humidity["dezumidificator"])

	# GPIO.cleanup()

