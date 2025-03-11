s = 0 
c = 0
for i in range(1,7):
    n = int(input('\033[1;35mDigite um numero: \033[m'))
    if n % 2 == 0:
        c += 1
        s += n
        
print(f'\033[1;35mA soma de todos os \033[1;32m{c} \033[1;35mnumeros pares e \033[1;32m{s}\033[m')
