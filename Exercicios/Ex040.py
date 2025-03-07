cor = {'limpa' : '\033[m',
       'red' : '\033[1;31m',
       'amarelo' : '\033[1;33m',
       'verde' : '\033[1;32m',
       'roxo' : '\033[1;35m'}
try:
    n1 = float(input(f'{cor['roxo']}Nota 1: {cor['limpa']}'))
    n2 = float(input(f'{cor['roxo']}Nota 2: {cor['limpa']}'))
    n3 = float(input(f'{cor['roxo']}Nota 3: {cor['limpa']}'))
except ValueError:
    print(f'{cor['red']}Entrada invalida!{cor['limpa']}')
    exit()

m = (n1 + n2 + n3) / 3

print(f'{cor['roxo']}Tirando {n1}, {n2} e {n3} a media do aluno e {m:.1f}{cor['limpa']}')
if m < 5.0:
    print(f'{cor['red']}ALUNO REPROVADO!{cor['limpa']}')   
elif m < 6.9:
    print(f'{cor['amarelo']}ALUNO EM RECUPERACAO!{cor['limpa']}')
else:
    print(f'{cor['verde']}ALUNO APROVADO!{cor['limpa']}')
