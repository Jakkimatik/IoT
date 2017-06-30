# Otetaan kayttoon RPi.GPIO-kirjasto
import RPi.GPIO as GPIO
# time-kirjasto
import time
# gpiozero-kirjaston osat LED ja TrafficLights helpottamaan komponenttien ohjausta
from gpiozero import LED, TrafficLights

GPIO.setmode (GPIO.BCM)

# Maaritetaan pinnit painikkeelle ja sensorille, seka liikennevalot (lights) ja jalankulkijoiden valot (red, green) gpiozero-komponentteina
PAINIKE=20
PIR=23
lights = TrafficLights(19,5,22)
red = LED(4)
green = LED(26)

# Asetetaan painikkeen seka PIR-sensorin pinnit sisaantulotilaan
GPIO.setup (PAINIKE, GPIO.IN)
GPIO.setup (PIR, GPIO.IN)

# Funktio valojen vaihtumis -sekvenssille
def valot():
	lights.green.off()
	lights.amber.on()
	time.sleep(2)
	lights.amber.off()
	lights.red.on()
	red.off();
	green.on();
	time.sleep(5)
	lights.red.off()
	lights.amber.on()
	time.sleep(2)
	green.off()
	lights.amber.off()
	return

# Aluksi autoilijoille palaa vihrea, jalankulkijoille punainen - nappia painettaessa luetaan PIR-sensorin tila ja jos liiketta ei havaita, valot vaihtuvat.
# Jos liiketta on, odotetaan 10 sekuntia ja tarkistetaan sensorin tila uudestaan - jos liiketta on edelleen, odotetaan viela toiset 10 sekuntia jonka jalkeen valot viimein vaihtuvat.
while True:
	lights.green.on()
	red.on()
	if GPIO.input (PAINIKE):
		i=GPIO.input (PIR)
		if i==0:
			valot()
		elif i==1:
			print "Odotetaan 10 sekuntia"
			time.sleep(10)
			a=GPIO.input (PIR)
			if a==0:
				valot()
			elif a==1:
				print "Toiset 10 sekuntia"
				time.sleep(10)
				valot()

# Loppusiivous
GPIO.cleanup ()
