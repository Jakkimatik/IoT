import RPi.GPIO as GPIO
# Otetaan kayttoon sensorin lukemiseen tarvittava kirjasto
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)

# Asetetaan sensoriksi Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT11

# Kaytetaan pinnia GPIO26
pin = 26

# Yritetaan lukea sensoria. Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    
GPIO.cleanup()
