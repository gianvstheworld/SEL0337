#usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setwarnings(False)

while True:
    GPIO.output(18, GPIO.HIGH)
    sleep(3)
    GPIO.output(18, GPIO.LOW)
    sleep(3)