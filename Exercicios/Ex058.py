from random import randint
c = randint(1,10)
cor = {'roxo' : '\033[1;35m',
       'red' : '\033[1;31m',
       'amarelo' : '\033[1;33m',
       'limpa' : '\033[m',
       'cyan' : '\033[1;36m',
       'blue' : '\033[1;34m',
       'verde' : '\033[1;32m',
       'erro' : '\033[4;31m'}
lin = f'{cor['amarelo']}=-{cor['limpa']}'*30
print(lin)
print(f'{cor['roxo']}{"JOGO DE ADIVINHACAO":^60}{cor['limpa']}')
print(lin)
print(f'{cor['roxo']}O computador escolhera um numero de 1 a 10\n'
       'Tente adivinhar qual e o numero.')
print(lin)
p = int(input(f'{cor['roxo']}Escolha um numero: {cor['limpa']}'))
palpites = 1
while p != c:
    palpites += 1
    if p < c:
       p = int(input(f'{cor['red']}Mais... {cor['roxo']}Tente de novo: {cor['limpa']}'))
    else:
       p = int(input(f'{cor['red']}Menos... {cor['roxo']}Tente de novo: '))    
print(f'{cor['verde']}O computador escolheu {c} {cor['limpa']}')
print(f'{cor['verde']}Parabens! Voce acertou o numero.{cor['limpa']}')
print(f'{cor['verde']}Foram nescessarios {palpites} palpites para voce acertar')
