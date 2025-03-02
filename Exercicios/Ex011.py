from math import ceil
lar = float(input('\033[1;34mInforme quantos metros de largura tem a parede? \033[m'))
alt = float(input('\033[1;34mInforme quantos metros de altura tem a parede? \033[m'))

litros_tinta = (lar * alt) / 2

cor = {'limpa' : '\033[m',
       'roxo' : '\033[1;35m',
       'ciano' : '\033[1;36m'}

print(f'{cor['roxo']}A parede tem {lar}m de largura e {alt}m de altura.{cor['limpa']}')
print(f'{cor['ciano']}Sera nescessario {ceil(litros_tinta)}l para pintar essa parede de {lar*alt}m2.{cor['limpa']}')

