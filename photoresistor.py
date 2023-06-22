import RPi.GPIO as GPIO

def get_light_state():
    # Definirea pinului pentru senzorul de lumină
    LIGHT_SENSOR = 15

    # Configurarea modului GPIO și a pinului pentru senzorul de lumină
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT_SENSOR, GPIO.IN)

    # Citirea stării senzorului de lumină
    is_light = GPIO.input(LIGHT_SENSOR)

    return is_light

