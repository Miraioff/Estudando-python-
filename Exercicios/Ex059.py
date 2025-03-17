from time import sleep
cor = {'roxo' : '\033[1;35m',
       'red' : '\033[1;31m',
       'amarelo' : '\033[1;33m',
       'limpa' : '\033[m',
       'cyan' : '\033[1;36m',
       'blue' : '\033[1;34m',
       'verde' : '\033[1;32m',
       'erro' : '\033[4;31m'}
lin = f'{cor['amarelo']}-={cor['limpa']}'*12
n1 = int(input(f'{cor['roxo']}Numero 1: {cor['limpa']}'))
n2 = int(input(f'{cor['roxo']}Numero 2: {cor['limpa']}'))
op = 0
while not op == 5:
    print(lin)
    print(f'''{cor['verde']}[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] ENCERRAR PROGRAMA{cor['limpa']}''')
    op = int(input(f'{cor['roxo']}Escolha uma opcao: {cor['limpa']}'))
    if op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print(f'{cor['erro']}Opcao Invalida.Tente novamente.{cor['limpa']}')
    if op == 1:
        print(f'{cor['cyan']}O resultado entre {n1} + {n2} e {n1 + n2}{cor['limpa']}')
    elif op == 2:
        print(f'{cor['blue']}O resultado de {n1} x {n2} e {n1 * n2}{cor['limpa']}')
    elif op == 3:
        if n1 > n2:
            print(f'{cor['red']}O numero {n1} e maior que {n2}{cor['limpa']}')
        elif n1 < n2:
            print(f'{cor['red']}O numero {n2} e maior que {n1}{cor['limpa']}')
        else:
            print(f'{cor['red']}Os numeros inserido sao iguais.{cor['limpa']}')
    elif op == 4:
        print(f'{cor['roxo']}informe os valores novamente.{cor['limpa']}')
        n1 = int(input(f'{cor['roxo']}Numero 1: {cor['limpa']}'))
        n2 = int(input(f'{cor['roxo']}Numero 2: {cor['limpa']}'))
print(f'{cor['roxo']}FINALIZANDO...{cor['limpa']}')
sleep(1.5)
print(f'{cor['roxo']}FIM DO PROGRAMA!{cor['limpa']}')
