from time import sleep
nome = str(input('\033[1;35mDigite seu nome completo: \033[m')).strip().title()
print('\033[1;32;43mAnalisando seu nome ...\033[m')
sleep(2)
print(f'\033[1;35mSeu nome em maiuscula e {nome.upper()}. \033[m')
print(f'\033[1;35mSeu nome em minuscula e {nome.lower()}. \033[m')
print(f'\033[1;35mSeu nome tem ao todo {len(nome) - nome.count(' ')} letras.\033[m')
print(f'\033[1;35mSeu primeiro nome e {nome.split()[0]} e ele tem {len(nome.split()[0])} letras. \033[m')
