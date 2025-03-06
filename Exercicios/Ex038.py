from time import sleep
try:
    n1 = int(input('\033[1;36mFirst number: \033[m'))
    n2 = int(input('\033[1;36mSecond number: \033[m'))
except ValueError:
    print('\033[1;31mInvalid input! Only integer values will be accepted.\033[m')
    exit()
print('\033[1;36mANALYZING...\033[m')
sleep(2)
if n1 > n2:
    print('\033[1;36mThe first value is greater.\033[m')
elif n2 > n1:
    print('\033[1;36mThe second value is greater.\033[m')
else:
    print('\033[1;36mThe two values are equal.\033[m')