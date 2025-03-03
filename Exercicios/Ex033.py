n1 = int(input('\033[1;35mPrimeiro valor: \033[m'))
n2 = int(input('\033[1;35mSegundo valor: \033[m'))
n3 = int(input('\033[1;35mTerceiro valor: \033[m'))
#verificando o menor numero
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'\033[1;32mO menor valor digitado foi {menor}\033[m')
# verificando o maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'\033[1;33mO maior valor digitado foi {maior}\033[m')

