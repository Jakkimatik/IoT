# Otetaan kayttoon RPi.GPIO-kirjasto
import RPi.GPIO as GPIO
# time-kirjaston sleep-toiminto
from time import sleep
# gpiozero-kirjaston osat LED ja TrafficLights helpottamaan komponenttien ohjausta
from gpiozero import LED, TrafficLights

GPIO.setmode (GPIO.BCM)

# Maaritetaan painike, liikennevalot (lights) seka jalankulkijoiden valot (red, green)
PAINIKE=20
lights = TrafficLights(19,5,22)
red = LED(4)
green = LED(26)

# Asetetaan painikkeeseen kytketty pinni sisaantulotilaan
GPIO.setup (PAINIKE, GPIO.IN)

# Aluksi autoilijoille palaa vihrea, jalankulkijoille punainen - nappia painettaessa ensin keltainen signaalivalo syttyy 2 sekunniksi jonka jalkeen valot vaihtuvat 5 sekunniksi
while True:
	lights.green.on()
	red.on()
	if GPIO.input (PAINIKE):
		sleep(1)
		lights.green.off()
		lights.amber.on()
		sleep(2)
		lights.amber.off()
		lights.red.on()
		red.off();
		green.on();
		sleep(5)
		lights.red.off()
		lights.amber.on()
		sleep(2)
		green.off()
		lights.amber.off()

# Loppusiivous
GPIO.cleanup ()
