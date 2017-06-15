import RPi.GPIO as GPIO
import time
# Otetaan kayttoon kamera-kirjasto
import picamera

GPIO.setmode(GPIO.BCM)

# Luetaan BCM-pinnissa 11 kiinni olevaa PIR-sensoria
GPIO.setup(11, GPIO.IN)

# Maaritetaan kamera
camera = picamera.PiCamera()

# Pyoritetaan while-silmukkaa 15 sekunnin ajan
loppu = time.time() + 15
while time.time() < loppu:
# Luetaan sensorin tilaa muuttujaan i ja tulostetaan sen mukaan havaintoja ruudulle sekunnin valein.
# Otetaan kuva jos havaitaan liiketta. Havaitsin etta kerran liiketta tunnistettuaan sensorin tila == 1 ainakin n. 5 sekunnin ajan
# joten voitaisiin yhta hyvin nukkua sen aikaa (time.sleep(5)).
    i=GPIO.input(11)
    if i==0:
        print "Ei havaita liiketta"
        time.sleep(1)
    elif i==1:
		camera.capture('kuva' + time.asctime() + '.jpg')
		time.sleep(5)

GPIO.cleanup()
