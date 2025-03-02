import math 
a = float(input('\033[1;33minforme o valor de um angulo: '))
#transformacao de graus para radianos
an = math.radians(a)

cor = {'limpa' : '\033[m',
       'red' : '\033[1;31m',
       'verde' : '\033[1;32m',
       'azul' : '\033[1;34m'}

print(f'{cor['azul']}O valor de seno {math.sin(an):.1f}{cor['limpa']}')
print(f'{cor['red']}O valor de cosseno e {math.cos(an):.1f}{cor['limpa']}')
print(f'{cor['verde']}O valor da tengente e {math.tan(an):.1f}{cor['limpa']}')
