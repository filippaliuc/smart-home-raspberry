from tempAndHumidity import getHumidityAndTemperature
from photoresistor import getLightIntensity
from distanceSensor import getDistance
from firebase import database
import time

try: 
    while True:
        temperature, humidity = getHumidityAndTemperature()
        isLight = getLightIntensity()
        distance = getDistance()

        data = {
            "temperatura(C)":temperature,
            "umiditate(%)":humidity,
            "lumina":isLight,
            "distanta(cm)":distance
        }

        database.child("semnale").set(data)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nDone")
