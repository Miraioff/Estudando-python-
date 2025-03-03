from time import sleep
n = int(input('\033[1;35mMe diga um numero qualquer: \033[m'))
print('\033[1;35mANALISANDO...\033[m')
sleep(3)
if n % 2 == 0:
    print(f'\033[1;32mO numero {n} e par.\033[m')
else:
    print(f'\033[1;33mO numero {n} e impar.\033[m')
