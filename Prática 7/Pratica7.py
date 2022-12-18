from smbus import SMBus

addr = 0x8
bus = SMBus(1)

flag = 1

'''
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

dados = bus.read_i2c_block_data(addr, 0, 2)
soma = 256*dados[0] + dados[1]
print(dados, soma) 