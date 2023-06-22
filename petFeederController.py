import RPi.GPIO as GPIO
from time import sleep
from firebase import database

# Definirea pinilor GPIO pentru umidificator și dezumidificator
#INPUT1_PIN = 16
#INPUT2_PIN = 18

# Configurarea modului GPIO și a pinilor
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(INPUT1_PIN, GPIO.OUT)
#GPIO.setup(INPUT2_PIN, GPIO.OUT)


def feed_cat():
    # Controlul stării pinilor GPIO în funcție de valorile umidificatorului și dezumidificatorului
    GPIO.output(INPUT1_PIN, GPIO.LOW)
    GPIO.output(INPUT2_PIN, GPIO.LOW)

    while True:
        prediction = database.child("predictie").child("tip").get()
        if prediction.val() == "Cat":
            print("Cat")
            GPIO.output(INPUT2_PIN, GPIO.HIGH)
            sleep(10)
            GPIO.output(INPUT2_PIN, GPIO.LOW)
        sleep(30 * 60)

def feed_dog():

    # Controlul stării pinilor GPIO în funcție de valorile umidificatorului și dezumidificatorului
    GPIO.output(INPUT1_PIN, GPIO.LOW)

    while True:
        prediction = database.child("predictie").child("tip").get()
        if prediction.val() == "Dog":
            print("Dog")
            GPIO.output(INPUT1_PIN, GPIO.HIGH)
            sleep(10)
            GPIO.output(INPUT1_PIN, GPIO.LOW)
        sleep(30 * 60)

