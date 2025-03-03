nome = str(input('\033[1;36mDigite seu nome completo: \033[m')).strip().title()
print('\033[1;36mPrazer em te conhecer!\033[m')
print(f'\033[1;36mSeu primeiro nome e {nome.split()[0]}.\033[m')
print(f'\033[1;36mSeu ultimo nome e {nome.split()[-1]}.\033[m')
