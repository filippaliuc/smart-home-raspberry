import RPi.GPIO as GPIO
from time import sleep

input1Pin = 16
input2Pin = 18

def controlHumidity(humidity):

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(input1Pin, GPIO.OUT)
	GPIO.setup(input2Pin, GPIO.OUT)
	print("ceva")
	if(humidity < 50):
		print("ceva")	
		GPIO.output(input1Pin, GPIO.HIGH)
		GPIO.output(input2Pin, GPIO.LOW)
	else:
		print("altceva")
		GPIO.output(input1Pin, GPIO.LOW)
		GPIO.output(input2Pin, GPIO.HIGH)
	
controlHumidity(80)
sleep(5)
controlHumidity(40)
sleep(5)
GPIO.cleanup()
