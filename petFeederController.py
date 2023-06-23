import RPi.GPIO as GPIO
from time import sleep
from firebase import database

def feed_cat():
    # Definirea pinilor GPIO pentru umidificator și dezumidificator
    INPUT1_PIN = 33

    # Configurarea modului GPIO și a pinilor
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT1_PIN, GPIO.OUT)

    # Controlul stării pinilor GPIO în funcție de predicție
    GPIO.output(INPUT2_PIN, GPIO.HIGH)

    while True:
        prediction = database.child("predictie").child("tip").get()
        if prediction.val() == "Cat":
            GPIO.output(INPUT2_PIN, GPIO.LOW)
            print("Cat")
            sleep(10)
            GPIO.output(INPUT2_PIN, GPIO.HIGH)
        sleep(30 * 60)

def feed_dog():
    # Definirea pinilor GPIO pentru umidificator și dezumidificator
    INPUT2_PIN = 35

    # Configurarea modului GPIO și a pinilor
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT2_PIN, GPIO.OUT)
    
    # Controlul stării pinilor GPIO în funcție de predicție
    GPIO.output(INPUT1_PIN, GPIO.HIGH)

    while True:
        prediction = database.child("predictie").child("tip").get()
        if prediction.val() == "Dog":
            print("Cat")

            GPIO.output(INPUT1_PIN, GPIO.LOW)
            sleep(10)
            GPIO.output(INPUT1_PIN, GPIO.HIGH)
        sleep(30 * 60)

