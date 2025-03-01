al = input('\033[1;35mDigite algo: ')
cores = {'limpa' : '\033[m',
         'roxo' : '\033[1;35m'}

print(f'{cores['roxo']} O tipo primitivo desse valor e {cores['limpa']} {type(al)} ')
print(f'{cores['roxo']} So tem espacos? {cores['limpa']} {al.isspace()}')
print(f'{cores['roxo']} E um numero? {cores['limpa']} {al.isnumeric()}')
print(f'{cores['roxo']} E alfabetico? {cores['limpa']} {al.isalpha()}')
print(f'{cores['roxo']} E alfanumerico? {cores['limpa']} {al.isalnum()}')
print(f'{cores['roxo']} Esta em maiusculas? {cores['limpa']} {al.isupper()}')
print(f'{cores['roxo']} Esta em minusculas? {cores['limpa']} {al.islower()}')
print(f'{cores['roxo']} Esta capitalizada? {cores['limpa']} {al.istitle()}')
