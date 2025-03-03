from time import sleep
dis = float(input('\033[1;35mInforme a distancia da viagem [km]: \033[m'))
print('\033[1;43mCALCULANDO...\033[m')
sleep(3)
print(f'Voce esta prestes a iniciar uma viajem de \033[1;43m{dis:.1f}km\033[m')
if dis > 200:
    print(f'O valor da sua passagem sera de \033[1;43mR${dis*0.45:.2f}\033[m')
else:
    print(f'O valor da sua passagem sera de \033[1;43mR${dis*0.50:.2f}\033[m')

