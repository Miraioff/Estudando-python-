cores = {'limpa' : '\033[m',
         'roxo' : '\033[1;35m',
         'amarelo' : '\033[1;33m',
         'verde' : '\033[1;32m'}
n = int(input('\033[1;35mDigite um numero: '))
print(f'{cores['amarelo']}O antecessor de {n} e {n-1}. {cores['limpa']}')
print(f'{cores['verde']}O sucessor de {n} e {n+1}. {cores['limpa']}')

