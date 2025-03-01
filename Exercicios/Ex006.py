from math import sqrt
n = int(input('\033[1;53mDigite um numero: \033[m'))
cor = {'azul' : '\033[1;34m',
       'roxo' : '\033[1;35m',
       'ciano' : '\033[1;36m',
       'limpa' : '\033[m'}
print(f'{cor['azul']}O dobro de {n} e {n*2} . {cor['limpa']}')
print(f'{cor['roxo']}O triplo de {n} e {n*3} . {cor['limpa']}')
print(f'{cor['ciano']}A raiz quadrada de {n} e {sqrt(n)} . {cor['limpa']}')

