import RPi.GPIO as GPIO
import time

servo_pin = 4 # definindo o pino do servo

GPIO.setmode(GPIO.BCM) # setando o modo de funcionamento da placa
GPIO.setup(servo_pin, GPIO.OUT) # colocando como pino de saída o servo

freq = 1000/100 # f = 1/T = 1/0.1
duty_zero = 5 # duty cycle inicial
pulso = 20 # largura do pulso

pwm = GPIO.PWM(servo_pin, freq) # definindo o PWM 
pwm.start(0) # inicializando o PWM

try:
    while True:
        bright = float(input('Insira a luminosidade (Entre 0 e 425): '))
        duty = duty_zero + bright/100 * pulso # cálculo da luminosidade do LED
        pwm.ChangeDutyCycle(duty) # alteração do duty cycle de acordo com a luminosidade escolhida
finally:
    GPIO.cleanup() # limpando os pinos de uso toda vez que o código é finalizado
        

