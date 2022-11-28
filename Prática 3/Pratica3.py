from gpiozero import LED
from time import sleep 

vermelho = LED(18)

try:
    tempo = int(input("Defina um tempo para contagem regressiva de ativação do LED: "))
except ValueError as e:
    print(e)

min, seg = divmod(tempo,60)

if tempo > 0:
    if min > 0 and seg >= 0:
        print(f"A contagem regressiva é de {min}min e {seg}s")
    else:
        print(f"A contagem regressiva é de {seg}s") 

    while(True):
        vermelho.on()
        sleep(tempo)
        vermelho.off()
        sleep(tempo)
else:
    print("Valor de entrada errado!")
