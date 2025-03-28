color = {
    'clear' : '\033[m',
    'purple' : '\033[1;35m',
    'yellow' : '\033[1;33m'
}
line = f'{color["yellow"]}-={color["clear"]}'*20
print(line)
print(f'{color["purple"]}{"CAIXA ELETRONICO":^40}{color["clear"]}')
print(line)
value = int(input(f'{color["purple"]}Qual valor voce quer sacar? R$'))
total = value
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{color["purple"]}Total de {totced} cedulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print(line)

