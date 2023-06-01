import Adafruit_DHT
from firebase import database

def getHumidityAndTemperature():
    humidity, temperature = Adafruit_DHT.read_retry(11,4)

    print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature,humidity))
    
    data = {
        "temperatura(C)":temperature,
        "umiditate(%)":humidity
    }

    # database.child("semnale").set(data)

    return temperature, humidity
