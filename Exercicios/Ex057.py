sexo = ''
sexo = str(input('\033[1;35mDigite seu sexo [M/F] : \033[m')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    # sexo not in 'MmFf
    sexo = str(input('\033[1;31mDado invalido. \033[1;35mDigite seu sexo: [M/F] \033[m')).strip().upper()[0]
print(f'\033[1;32mSexo \033[1;35m{sexo} \033[1;32mregistrado com sucesso.\033[m')
