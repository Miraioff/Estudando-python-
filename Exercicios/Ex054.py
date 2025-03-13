from datetime import date
cor = {'roxo' : '\033[1;35m',
       'limpa' : '\033[m',
       'cyan' : '\033[1;36m'}
atual = date.today().year 
smi = 0
si = 0
for i in range(1,8):
    ano = int(input(f'{cor['roxo']}Informe o ano em que a {i}.o pessoa nasceu: {cor['limpa']}'))
    i = atual - ano
    if i >= 21:
        smi += 1
    else:
        si += 1
print(f'{cor['cyan']}{smi}{cor['roxo']} pessoas sao maiores de idade.{cor['limpa']}')
print(f'{cor['roxo']}E {cor['cyan']}{si} {cor['roxo']}pessoas sao menores de idade.{cor['limpa']}')
