lin = f'\033[1;36m-=\033[m'*20

print(lin)
print(f'\033[1;35m{"10 TERMOS DE UMA PA":^40}\033[m')
print(lin)

pt = int(input('\033[1;35mPrimeiro Termo: \033[m'))
r = int(input('\033[1;35mRazao : \033[m'))
# calcula o decimo termo da PA
d = pt + (10 - 1) * r
for i in range(pt,d + r,r):
    print(f'\033[1;32m{i}',end=' -> ')
print('\033[1;33mACABOU\033[m')
