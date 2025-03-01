cor = {'limpa' : '\033[m',
       'ciano' : '\033[1;36m'}

n1 = float(input('\033[1;31mNota 1: \033[m'))
n2 = float(input('\033[1;31mNota 2: \033[m'))
print(f'{cor['ciano']}A media do aluno e {(n1+n2)/2:.1f} {cor['limpa']}')
