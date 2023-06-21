import Adafruit_DHT

def get_temperature_and_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(11,4)

    return temperature, humidity
