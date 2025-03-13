maior_peso = 0
menor_peso = 9999999
for pessoa in range(1,6):
    peso = float(input(f'\033[1;36mPeso da {pessoa}.o pessoa: \033[m'))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print(f'\033[1;31mO maior peso lido foi {maior_peso}kg \033[m')
print(f'\033[1;33mO menor peso lido foi {menor_peso}kg \033[m')
