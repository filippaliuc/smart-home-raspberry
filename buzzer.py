import RPi.GPIO as GPIO
import math
from time import sleep	
from flameSensor import get_flame

# Funcția utilizată pentru firul de execuție care pornește alarma sau oprește alarma
def trigger_fire_alarm():

	# Pinul pentru buzzer
	BUZZER_PIN = 22

	# Inițializarea modului de numerotare al pinilor
	GPIO.setmode(GPIO.BOARD)

	# Configurarea pinului pentru buzzer ca ieșire
	GPIO.setup(BUZZER_PIN, GPIO.OUT)

	global PWM

	# Crearea obiectului PWM pentru pinul buzzer cu o frecvență inițială de 1 Hz
	PWM = GPIO.PWM(BUZZER_PIN, 1)
	PWM.start(0)

	while True:
		# Obținerea stării senzorului de flăcări
		is_flame = get_flame()

		if not is_flame:
			# Pornirea PWM la 50% pentru a genera sunetul de alarmă
			PWM.start(50)

			# Generarea sunetului de alarmă
			for x in range(0, 361):
				sin_val = math.sin(x * (math.pi / 180))

				# Calcularea valorii tonului bazat pe valoarea sinusului
				tone_val = 2000 + sin_val * 500

				# Modificarea frecvenței PWM pentru a genera tonul corespunzător
				PWM.ChangeFrequency(tone_val)
				sleep(0.001)
		else:
			# Oprirea PWM în cazul în care nu se detectează flăcări
			PWM.stop()
