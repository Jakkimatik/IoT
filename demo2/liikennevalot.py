# Otetaan kayttoon RPi.GPIO-kirjasto
import RPi.GPIO as GPIO
# ja time-kirjaston sleep-toiminto
from time import sleep
# Kaytetaan gpiozero-kirjaston osia LED, Button ja TrafficLights helpottamaan komponenttien ohjausta
from gpiozero import LED, Button, TrafficLights

GPIO.setmode (GPIO.BCM)

# Maaritetaan painike, autoilijoiden liikennevalot (lights) seka jalankulkijoiden valot (red, green) gpiozero-kirjaston komponentteina
button = Button(20)
lights = TrafficLights(19,5,22)
red = LED(4)
green = LED(26)

# Aluksi autoilijoille palaa vihrea, jalankulkijoille punainen valo - nappia painettaessa keltainen ja jalankulkijoiden punainen valkkyvät sekunnin ajan, jonka jalkeen valot vaihtuvat 7 sekunniksi
while True:
	lights.green.on()
	red.on()
	button.wait_for_press()
	sleep(1)
	lights.green.off()
	lights.amber.blink(0.2, 0.2)
	red.blink(0.1, 0.2)
	sleep(1)
	lights.amber.off()
	lights.red.on()
	red.off();
	green.on();
	sleep(7)
	lights.red.off()
	lights.amber.on()
	green.blink(0.1, 0.2)
	sleep(1)
	green.off()
	lights.amber.off()   

# Loppusiivous
GPIO.cleanup ()

