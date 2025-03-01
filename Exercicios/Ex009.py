n = int(input('\033[7;30mDigite um numero para saber sua tabuada: '))
cor = {'limpa' : '\033[m',
       'verde' : '\033[1;32;43m',
       'amarelo' : '\033[1;33;42m'}
print(f'{cor['amarelo']}={cor['limpa']}'*20)
print(f'{cor['amarelo']}TABUADA DO {n}        {cor['limpa']}')
print(f'{cor['amarelo']}={cor['limpa']}'*20)

for x in range(1,11):
    print(f'{cor['amarelo']}{n} X {x:2} = {n*x:2}         {cor['limpa']}')
print(f'{cor['amarelo']}={cor['limpa']}'*20)
