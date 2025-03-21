color = {'purple' : '\033[1;35m',
         'blue' : '\033[1;34m',
         'clear' : '\033[m'}
n = int(input(f'{color['purple']}Enter an integer (999 stop): '))
c = 0
s = 0
while n != 999:
    s += n
    c += 1
    n = int(input(f'{color['purple']}Enter an integer (999 stop): '))
print(f'{color['blue']}{c} {color['purple']}numbers were entered, and the sum between them is {color['blue']}{s}{color['clear']}')
