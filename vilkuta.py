# Tuodaan RPi.GPIO-kirjasto koodiin.
import RPi.GPIO as GPIO
# Tuodaan ajankayttoon liittyva kirjasto
import time as timer
GPIO.cleanup ()
# Asetetaan BCM-numerointi
GPIO.setmode (GPIO.BCM)
# Asetetaan pinni 4 ulostulotilaan 
GPIO.setup (4, GPIO.OUT)
# Laitetaan pinniin 4 virtaa
GPIO.output (4, 1)
timer.sleep (0.5)
GPIO.output (4, 0)
timer.sleep (0.5)
GPIO.output (4, 1)
timer.sleep (0.5)
GPIO.output (4, 0)
# Lopuksi siivotaan jaljet  
GPIO.cleanup ()
