cit = str(input('\033[1;33mEm qual cidade voce nasceu: ')).strip().title()
com = cit.split()
print(f'\033[1;33mA cidade em que voce nasceu começa com o nome "Santo"? {'Santo' in com[0]} \033[m')
