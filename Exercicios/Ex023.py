from math import trunc
n = int(input('\033[1;34mDigite um numero inteiro qualquer entre 0 e 9999: \033[m'))

u = n % 10
d = (n % 100) / 10
c = (n % 1000) / 100
m = n / 1000

print(f'\033[1;45mUnidade: {u}')
print(f'\033[1;45mDezena:  {trunc(d)}\033[m')
print(f'\033[1;45mCentena: {trunc(c)}\033[m')
print(f'\033[1;45mMilhar:  {trunc(m)}\033[m')
