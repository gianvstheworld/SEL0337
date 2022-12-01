# Prática 5 
import threading, time, RPi.GPIO as GPIO # Importando algumas bibliotecas 

# Definição dos pinos
BUTTON_GPIO = 16
LED_GPIO = 20

# Configuração dos pinos
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GPIO, GPIO.OUT)

# Definição da variável que determina o estado do LED
blink = True

def red(T):
    '''
    Função que acende o LED 
    vermelho por T segundos
    '''
    global blink
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
    print('Botão pressionado!')

    global blink
    if blink:
        T = int(input('Escolha uma frequência para o LED piscar: '))
        print(f'T = {T}')
        red(T)

def timer_callback():
    global blink
    blink = False
    print('Tempo da thread esgotado')

if __name__ == '__main__':
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, callback = button_callback, bouncetime = 100)# Interpretação da interrupção do botão

    tr = threading.Timer(35.0, timer_callback)
    tr.start()

    red(1)
    
    
    

