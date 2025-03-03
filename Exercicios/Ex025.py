nome = str(input('\033[1;35mDigite seu nome completo: \033[m')).strip().title()
print(f'\033[1;35mSeu nome tem "Silva"? {'Silva' in nome}\033[m')
