# Otetaan kayttoon RPi.GPIO- seka time-kirjastot.
import RPi.GPIO as GPIO
import time

# LEDiin tulee virtaa pinnista #20 ja painikkeeseen pinnista #6
LED=20
PAINIKE=6

# Asetetaan BCM-numerointi
GPIO.setmode (GPIO.BCM)
# Asetetaan LEDin anodiin kytketty pinni ulostulotilaan
GPIO.setup (LED, GPIO.OUT)
# Asetetaan painikkeeseen kytketty pinni sisaantulotilaan
GPIO.setup (PAINIKE, GPIO.IN)

# Ajankohta nimeltaan 'loppu' on n. 10 sekunnin paassa skriptin ajohetkesta
loppu = time.time() + 10
# Annetaan virtaa LED-pinnille kun painike on pohjassa
# (eli kun GPIO.input (PAINIKE) = 1) kunnes ollaan ajankohdassa 'loppu'
while time.time() < loppu:
	GPIO.output(LED, GPIO.input (PAINIKE))
	time.sleep (0.1) # ilman tata prossukaytto 100%

# Loppusiivous
GPIO.cleanup ()
