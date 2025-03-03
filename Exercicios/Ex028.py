from time import sleep
from random import randint
print(f'\033[1;31m=\033[1;31m'*64)
print(f'\033[1;35mJOGO DE ADVINHAÇÃO\033[m')
print(f'\033[1;31m=\033[1;31m'*64)
p = int(input('\033[1;35mIrei pensar em um numero entre 0 e 5, Tente descobrir qual e: \033[m'))
print('\033[1;35mPENSANDO...\033[m')
sleep(2)
c = randint(0,5)
if p not in range(6):
    print(f'\033[4;31mO numero {p} nao faz parte do jogo, Escolha entre 0 e 5.\033[m') 
    exit()
else:
    if p == c:
        print(f'\033[1;32mEu pensei no numero {c}, Parabens! voce venceu!\033[m')
    else:
        print(f'\033[1;35mEu nao pensei no numero {p}, Pensei no numero {c} Eu venci!\033[m')
print(f'\033[1;31m=\033[1;31m'*64)
print('FIM!')
