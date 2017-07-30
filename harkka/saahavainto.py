# Otetaan kayttoon RPi.GPIO-, Adafruit_DHT-, datetime- seka picamera-kirjastot
import RPi.GPIO as GPIO
import Adafruit_DHT
import datetime
import picamera

# Asetetaan BCM-numerointi
GPIO.setmode(GPIO.BCM)

# Asetetaan sensoriksi Adafruit_DHT.DHT11
sensori = Adafruit_DHT.DHT11

# Kaytetaan sensorin lukemiseen pinnia BCM 7 (Adafruit T-Cobbler Plus:salla pinni "CE1")
pin = 7

# Maaritetaan kamera
camera = picamera.PiCamera()
camera.resolution = (1024, 768)

# Luetaan sensoria read_retry-metodilla joka yrittaa lukea sensoria 15 kertaa kahden sekunnin valiajoin.
kosteus, lampotila = Adafruit_DHT.read_retry(sensori, pin)

# Jos lukeminen onnistuu, maaritetaan mittauksen ajankohta, otetaan saakuva ja kirjoitetaan tama kaikki HTML-dokumenttiin
if kosteus is not None and lampotila is not None:
	currentDT = datetime.datetime.now()
	camera.capture('/home/pi/IoT/harkka/havainnot/saakuva.jpg')
	with open("/home/pi/IoT/harkka/havainnot/index.htm", "w") as websivu:
		websivu.write('Lampotila: {0:0.1f} C <br> Kosteus: {1:0.1f} % <br>'.format(lampotila, kosteus))
		websivu.write('Mittauksen ajankohta: ');
		websivu.write(currentDT.strftime("%H:%M %Y-%m-%d"))
		websivu.write('<br><img src="saakuva.jpg"></img>');
