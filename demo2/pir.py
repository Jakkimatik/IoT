import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Luetaan BCM-pinnissa 11 kiinni olevaa PIR-sensoria
GPIO.setup(11, GPIO.IN)

# Pyoritetaan while-silmukkaa 30 sekunnin ajan
loppu = time.time() + 30
while time.time() < loppu:
# Luetaan sensorin tilaa muuttujaan i ja tulostetaan sen mukaan havaintoja ruudulle sekunnin valein.
# Havaitsin etta kerran liiketta tunnistettuaan sensorin tila == 1 ainakin n. 5 sekunnin ajan
# joten voitaisiin yhta hyvin nukkua sen aikaa (time.sleep(5)).
    i=GPIO.input(11)
    if i==0:
        print "Ei havaita liiketta"
        time.sleep(1)
    elif i==1:
        print "Liiketta havaittu"
        time.sleep(5)

GPIO.cleanup()
