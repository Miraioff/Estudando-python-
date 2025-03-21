color = {'purple' : '\033[1;35m',
         'yellow' : '\033[1;33m',
         'cyan' : '\033[1;36m'}
line = f'{color['yellow']}=-'*15
lowest_value = 999999999999
highest_value = 0
average = 0
leave = ''
s = 0
c = 0
while leave != 'N':
    print(line)
    n = int(input(f'{color['purple']}Enter integer: '))
    c += 1 
    s += n 
    if n < lowest_value:
        lowest_value = n
    if n  > highest_value:
        highest_value = n
    leave = str(input(f'{color['purple']}Do you want to continue[S/N]?')).strip().upper()[0]
average = s / c
print(line)
print(f'{color['purple']}The highest value entered was {color['cyan']}{highest_value}')
print(f'{color['purple']}The lowest value entered was {color['cyan']}{lowest_value}')
print(f'{color['purple']}The average of the values entered is {color['cyan']}{average:.1f}')
print(line)
