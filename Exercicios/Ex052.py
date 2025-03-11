n = int(input('\033[1;35mDigite um numero inteiro: \033[m'))
t = 0
for c in range(1,n + 1):
    # se o resto da divisao entre n e c for == 0 vai o numero ira ficar roxo
    #ou seja, os numero n e divisivel por todos os numero que ficarem roxo e os que nao ficaram vermelho
    if n % c == 0:
        print(f'\033[1;35m', end=' ')
        t += 1
    else:
        print('\033[1;31m', end=' ')
    # mostra os numeros de 1 ate o n ja imbuida com as cores
    print(f'{c}',end=' ')

print(f'\n\033[1;35mO numero {n} foi divisivel {t} vezes.\033[m')
# se n  for divisel apenas por 2 numero (1 e ele mesmo) ele sera primo
if  t == 2:
    print(f'\033[1;35mO numero {n} e PRIMO.\033[m')
else:
    print(f'\033[1;35mO numero {n} NAO e PRIMO.\033[m')
    