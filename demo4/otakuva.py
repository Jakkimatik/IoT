# Otetaan kayttoon kamera- ja aika-kirjastot
import picamera
import time

# Maaritetaan kamera
camera = picamera.PiCamera()

camera.capture('/home/pi/motion/keskella_liiketta.jpg')
