from datetime import date
atual = date.today().year
cor = {'red' : '\033[1;31m',
       'ama' : '\033[1;33m',
       'azu' : '\033[1;34m',
       'rox' : '\033[1;35m',
       'ver' : '\033[1;32m',
       'cya' : '\033[1;36m',
       'lim' : '\033[m'}
lin = f'{cor['rox']}=-{cor['lim']}'*25
print(lin)
print(f'{cor['cya']}{"COFEDERACAO NACIONAL DE NATACAO":^50}{cor['lim']}')
print(lin)

try:
    year = int(input(f'{cor['cya']}Ano de nascimento: {cor['lim']}'))
    if year < 0:
        print(f'{cor['red']}Entrada invalida!{cor['lim']}')
        exit()
except ValueError:
    print(f'{cor['red']}Entrada invalida!{cor['lim']}')
    exit()
print(lin)
age = atual - year
print(f'{cor['cya']}O atleta tem {age} anos.{cor['lim']}')
if age <= 9:
    print(f'{cor['ver']}ATLETA MIRIM!{cor['lim']}')
elif age <= 14:
    print(f'{cor['azu']}ATLETA INFANTIL!{cor['lim']}')
elif age <= 19:
    print(f'{cor['rox']}ATLETA JUNIOR!{cor['lim']}')
elif age <= 25:
    print(f'{cor['ama']}ATLETA SENIOR!{cor['lim']}')
else:
    print(f'{cor['red']}ATLETA MASTER!{cor['lim']}')
