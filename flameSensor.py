import RPi.GPIO as GPIO

def get_flame():

	# Definirea pinului GPIO pentru senzorul de flacără
    FLAME_SENSOR = 37

    # Configurarea modului GPIO și pinului pentru senzorul de flacără
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(FLAME_SENSOR, GPIO.IN)
    
    # Citirea stării senzorului de flacără
    is_flame = GPIO.input(FLAME_SENSOR)
    
    return is_flame
