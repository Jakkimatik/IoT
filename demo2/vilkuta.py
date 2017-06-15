# Otetaan kayttoon RPi.GPIO-kirjasto
import RPi.GPIO as GPIO
# seka ajankayttoon liittyva kirjasto
import time as timer
# Varmistus-cleanup alustaa mahdollisesti auki jaaneet virransyotot ym. - ei valiteta kaantajan virheilmoituksesta
GPIO.cleanup ()
# Asetetaan BCM-numerointi
GPIO.setmode (GPIO.BCM)
# Asetetaan pinni 4 ulostulotilaan 
GPIO.setup (4, GPIO.OUT)
# Annetaan pinniin 4 virtaa
GPIO.output (4, 1)
# Odotetaan puoli sekuntia
timer.sleep (0.5)
# Katkaistaan virta
GPIO.output (4, 0)
# Odotetaan taas puoli sekuntia, ja toistamalla sama uudestaan saadaan aikaan vilkkumista
timer.sleep (0.5)
GPIO.output (4, 1)
timer.sleep (0.5)
GPIO.output (4, 0)
# Siivous
GPIO.cleanup ()
