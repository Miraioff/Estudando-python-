color = {'purple' : '\033[1;35m',
         'clear' : '\033[m',
         'yellow' : '\033[1;33m',
         'green' : '\033[1;32m'}
line = f'{color['yellow']}-={color['clear']}'*20
print(line)
print(f'{color['purple']}{"FIBONACCI SEQUENCE":^40}{color['clear']}')
print(line)
n = int(input(f'{color['purple']}Do you want to show how many terms: '))
t1 = 0
t2 = 1
c = 3
print(f'{color['green']}{t1}{color['purple']} -> {color['green']}{t2}{color['clear']}', end='')
while c <= n:
    t3 = t1 + t2
    print(f'{color['purple']} -> {color['green']}{t3}{color['clear']}', end='')
    t1 = t2
    t2 = t3
    c += 1
print(f'{color['purple']} -> {color['green']} END {color['clear']}')
