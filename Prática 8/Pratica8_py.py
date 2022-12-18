#usr/bin/python

# Importando bibliotecas
import RPi.GPIO as GPIO
from time import sleep

# Configurações de GPIO da Rasp
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setwarnings(False)

# Loop infinito para funcionamento do LED
while True:
    GPIO.output(18, GPIO.HIGH)
    sleep(3)
    GPIO.output(18, GPIO.LOW)
    sleep(3)