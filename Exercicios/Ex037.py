linha = '\033[1;33m=-\033[m'*25
print(linha)
print(f'\033[1;35m{"NUMBER BASE CONVERTER":^50}\033[m')
print(linha)
num = int(input('\033[1;35mEnter any integer: \033[m'))
base = int(input('\033[1;35mChoose the conversion base. \n'
                 '[1] for BINARY.\n'
                 '[2] for OCTAL.\n'
                 '[3] for HEXADECIMAL.\n'
                 'Your option:\033[m'))
if base != 1 and  base != 2 and base != 3:
    print('\033[1;31mInvalid value! enter 1, 2 or 3.\033[m')
    exit()

if base == 1: 
    print(f'\033[1;35m{num} converted to binary is equal to {bin(num)[2:]}\033[m')
elif base == 2:
    print(f'\033[1;35m{num} converted to octal is equal to {oct(num)[2:]}\033[m')
else:
    print(f'\033[1;35m{num} converted to hexadecimal is equal to {hex(num)[2:]}\033[m')
print(linha)
