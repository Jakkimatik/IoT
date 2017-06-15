# Otetaan kayttoon kamera- ja aika-kirjastot
import picamera
import time

# Maaritetaan kamera
camera = picamera.PiCamera()

camera.capture('Kuva ' + time.asctime() + '.jpg')
