from random import randint
color = {
    'red' : '\033[1;31m',
    'blue' : '\033[1;34m',
    'cyan' : '\033[1;36m',
    'green' : '\033[1;32m',
    'clear' : '\033[m',
    'purple' : '\033[1;35m',
    'yellow' : '\033[1;33m'
}
line = f'{color["yellow"]}-={color["clear"]}'*35
print(line)
print(f'{color["purple"]}{"JOGO DE PAR OU IMPAR":^60}{color["clear"]}')
player = s = c = 0
esc = ''
while True:
    comp = randint(1,10)
    print(line)
    player = int(input(f'{color["cyan"]}Diga um valor: ')) 
    esc = str(input(f'{color["cyan"]}Par ou Impar? ')).strip().upper()
    while esc not in ['PAR','IMPAR']:
        esc = str(input(f'{color["cyan"]}Par ou Impar? ')).strip().upper()
    print(line)
    print(f'{color["cyan"]}Voce escolheu {player} e o computador escolheu {comp}. O total de',end=' ')
    s = player + comp
    print(s, end=' ')
    if s % 2 == 0:
        result = 'PAR'
        print(f'deu {result}')
        if esc == 'PAR':
            c += 1
            print(line)
            print(f'{color["green"]}VOCE VENCEU!{color["clear"]}')
            print(f'{color["cyan"]}Vamos jogar novamente ...{color["clear"]}')
        else:
            print(line)
            print(f'{color["red"]}VOCE PERDEU!{color["clear"]}')
            break
    else:
        result = 'IMPAR'
        print(f'deu {result}')
        if esc == 'IMPAR':
            c += 1
            print(line)
            print(f'{color["green"]}VOCE VENCEU!{color["clear"]}')
            print(f'{color["cyan"]}Vamos jogar novamente...{color["clear"]}')
        else:
            print(line)
            print(f'{color["red"]}VOCE PERDEU!{color["clear"]}')
            break
print(line)
print(f'{color["red"]}GAME OVER! {color["cyan"]}Voce venceu {c} vezes.{color["clear"]}')

