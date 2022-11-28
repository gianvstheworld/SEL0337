# Prática 5 
import threading, time, RPi.GPIO as GPIO # Importando algumas bibliotecas 

# Definição dos pinos
BUTTON_GPIO = 16
LED_GPIO = 20

# Definição da variável que determina o estado do LED
blink = True

def red(T):
    '''
    Função que acende o LED 
    vermelho por T segundos
    '''
    while blink:
        print("LED piscando T =", T)
        GPIO.output(LED_GPIO, GPIO.HIGH)
        time.sleep(T)
        GPIO.output(LED_GPIO, GPIO.LOW)        
        time.sleep(T)
        
def button_callback():
    '''
    Função que é chamada quando
    o botão é pressionado   
    '''
    if GPIO.input(BUTTON_GPIO):
        T = input('Botão pressionado!\nEscolha uma frequência para o LED piscar: ')
        print(f'T = {T}')
        red(T)

def timer_callback():
    print('Tempo da thread esgotado')
    global blink
    blink = False

if __name__ == '__main__':
    # Configuração dos pinos
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_GPIO, GPIO.OUT)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, callback = button_callback, bouncetime = 100)# Interpretação da interrupção do botão

    tr = threading.Timer(35.0, timer_callback)
    tr.start()

    red(1)
    
    
    

