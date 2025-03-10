lin = f'\033[1;33m=-\033[m'*20
print(lin)
print(f'\033[1;35m{"TABUADA":^40}\033[m')
print(lin)
n = int(input('\033[1;35mDigite um numero para saber a tabuada:\033[m'))
print(lin)
for i in range(1,11):
    print(f'\033[1;35m{n} X {i:2} = \033[1;32m{n*i}\033[m')
print(lin)