color = {
    'purple' : '\033[1;35m',
    'yellow' : '\033[1;33m',
    'cyan' : '\033[1;36m',
    'clear' : '\033[m'
}
line = f'{color['yellow']}-={color['clear']}'*25
s = c = 0
while True:
    print(line)
    n = int(input(f'{color['purple']}Enter a value (enter 999 to stop): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'{color['cyan']}The sum of the {c} values is {s}{color['clear']}')
