from time import sleep
km = float(input('\033[1;35mQuantos km foram percorridos com o carro? \033[m'))
d = int(input('\033[1;35mPor quantos dias o carro foi Alugado \033[m'))
#calculo do aluguel [cada km vale R$0.15] e [cada dia vale [R$60.00]]
valor = (km * 0.15) + (d * 60)
print('\033[1;34;45mCALCULANDO...\033[m')
sleep(2)
print(f'\033[1;36mO aluguel do carro custara R${valor:.2f} \033[m')
