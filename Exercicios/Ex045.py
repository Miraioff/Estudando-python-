from random import randint
from time import sleep
comp = randint(0,2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
cor = {'roxo' : '\033[1;35m',
       'red' : '\033[1;31m',
       'amarelo' : '\033[1;33m',
       'limpa' : '\033[m',
       'cyan' : '\033[1;36m',
       'blue' : '\033[1;34m',
       'verde' : '\033[1;32m',
       'cinza' : '\033[1;37m',
       'erro' : '\033[4;31m'}
lin = f'{cor["amarelo"]}=-{cor["limpa"]}'*20 
print(lin)
print(f'{cor['roxo']}{"JOKENPO":^40}{cor['limpa']}')
print(lin)
print(f'''{cor['roxo']}ESCOLHA
[0] PARA PEDRA
[1] PARA PAPEL
[2] PARA TESOURA{cor['limpa']}''')
try:
    esc = int(input(f'{cor['roxo']}Escolha: {cor['limpa']}'))
    if esc != 0 and esc != 1 and esc != 2:
        print(f'{cor['erro']}Escolha invalida!{cor['limpa']}')
        exit()
except ValueError:
    print(f'{cor['erro']}Entrada invalida! {cor['limpa']}')
    exit()
print(f'{cor['roxo']}JO')
sleep(1)
print(f'KEN')
sleep(1)
print(f'PO!!!{cor['limpa']}')
print(lin)
print(f'{cor['blue']}O computador escolheu {itens[comp]}{cor['limpa']}')
print(f'{cor['cyan']}O jogador escolheu {itens[esc]}{cor['limpa']}')
print(lin)
if comp == 0 and esc == 1 or comp == 1 and esc == 2 or comp == 2 and esc == 0:
    print(f'{cor['verde']}VOCE VENCEU!{cor['limpa']}')
elif comp == 1 and esc == 0 or comp == 2 and esc == 1 or comp == 0 and esc == 2:
    print(f'{cor['red']}VOCE PERDEU!{cor['limpa']}')
else:
    print(f'{cor['roxo']}EMPATE!{cor['limpa']}')
print(lin)
