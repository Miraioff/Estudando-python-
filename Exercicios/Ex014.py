from time import sleep
celsius = float(input('\033[1;30mQuantos °C esta fazendo na sua região? \033[m'))

fah = (celsius * 9 / 5) + 32 
k = celsius + 273.15

print(f'\033[1;32mCALCULANDO...\033[m')
sleep(3)
print(f'\033[1;32mA temperatura de {celsius:.2f}°c equivale a {fah:.1f}°F.\nE {k:.2f}Kelvin\033[m')
