m = float(input('\033[1;35mInforme uma medida em metros: '))
cor = {'limpa' : '\033[m',
       'verde' : '\033[1;32m',
       'red' : '\033[1;31m'}
print(f'{cor['red']}A distancia de {m:.1f}m equivale a {m*100}Cm. {cor['limpa']}')
print(f'{cor['verde']}A distancia de {m:.1f}m equivale a {m*1000}mm. {cor['limpa']}')