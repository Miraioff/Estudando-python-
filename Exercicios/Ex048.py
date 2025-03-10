s = 0
soma = 0 
for i in range(1,501):
    if i % 2 == 1 and i % 3 == 0:
        #soma 
        soma += i
        #conta quantos sao/contador
        s += 1 
         
print(f'\033[1;35mA soma de todos os \033[1;32m{s}\033[1;35m valores solicitado e \033[1;33m{soma}\033[m')