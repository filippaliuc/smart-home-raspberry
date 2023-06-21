import RPi.GPIO as GPIO

def get_light_state():

    LIGHT_SENSOR = 15

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT_SENSOR,GPIO.IN)

    is_light = GPIO.input(LIGHT_SENSOR)
    
    return is_light
    
