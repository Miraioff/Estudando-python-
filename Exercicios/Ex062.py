color = {'purple' : '\033[1;35m',
       'yellow' : '\033[1;33m',
       'clear' : '\033[m',
       'green' : '\033[1;32m'}

line =f'{color['yellow']}=-{color['clear']}'*20

print(line)
print(f'{color['purple']}{"PA GENERATOR":^40}{color['clear']}')
print(line)

first = int(input(f'{color['purple']}First term: '))
reason = int(input(f'{color['purple']}Reason: '))
c = 1
term = first
more = 10
t = 0
while more != 0:
    t += more
    while c <= t:
        print(f'{color['green']}{term}', end=f'{color['purple']} -> {color['clear']}')
        term += reason
        c += 1 
    print(f'{color['purple']}PAUSE{color['clear']}')
    more = int(input(f'{color['purple']}Want to add more terms? '))
print(f'{color['purple']}PA had a total of {t} terms.{color['clear']}')
print(f'{color['purple']}END{color['clear']}')