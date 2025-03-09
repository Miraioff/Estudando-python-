cor = {'roxo' : '\033[1;35m',
       'red' : '\033[1;31m',
       'amarelo' : '\033[1;33m',
       'limpa' : '\033[m',
       'cyan' : '\033[1;36m',
       'blue' : '\033[1;34m',
       'verde' : '\033[1;32m',
       'cinza' : '\033[1;37m',
       'erro' : '\033[4;31m'}
lin = f'{cor["cinza"]}=-{cor["limpa"]}'*25
print(lin)
print(f'{cor['cyan']}{"INDICE DE MASSA CORPOREA(IMC)":^50}{cor['limpa']} ')
print(lin)
try:
    peso = float(input(f'{cor['cyan']}Informe seu peso[kg]: {cor['limpa']}'))
    alt = float(input(f'{cor['cyan']}Informe sua altura[m]: {cor['limpa']}'))
    if peso <= 0 or alt <= 0:
        print(f'{cor['erro']}Entrada invalida!{cor['limpa']}')
        exit()
except ValueError:
    print(f'{cor['erro']}Entrada Invalida!{cor['limpa']}')
    exit()
print(lin)
imc = peso / (alt ** 2)
print(f'{cor['cyan']}Seu imc e {imc:.1f}{cor['limpa']}')
if imc < 18.5:
    print(f'{cor['roxo']}ABAIXO DO PESO{cor['limpa']}')
elif imc < 25:
    print(f'{cor['verde']}PESO IDEAL{cor['limpa']}')
elif imc < 30:
    print(f'{cor['blue']}SOBREPESO{cor['limpa']}')
elif imc < 40:
    print(f'{cor['amarelo']}OBESIDADE{cor['limpa']}')
else:
    print(f'{cor['red']}OBESIDADE MORBIDA{cor['limpa']}')
print(lin)
