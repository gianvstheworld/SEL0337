# Importando biblioteca para comunicação 
from smbus import SMBus

addr = 0x8 # Endereço do dispositivo 
bus = SMBus(1) # Inicializa o barramento 1

'''
# Variável para controlar o loop
flag = 1

# Envia um byte para o dispositivo
print("LED control: ")
while flag == 1:
    ledstate = int(input(""))
    
    if ledstate == 1:
        bus.write_byte(addr, 0x1)
    elif ledstate == 0:
        bus.write_byte(addr, 0x0)
    else:
        flag = 0
'''

dados = bus.read_i2c_block_data(addr, 0, 2) # Recebe um byte do dispositivo
soma = 256*dados[0] + dados[1] # Calcula a soma dos bytes recebidos
print(dados, soma) 