color = {
    'clear' : '\033[m',
    'cyan' : '\033[1;36m',
    'purple' : '\033[1;35m',
    'yellow' : '\033[1;33m',
}

line = f'{color["yellow"]}=-{color["clear"]}'*32

n = 0

while True:
    print(line)
    n = int(input(f'{color["purple"]}Do you want to see the multiplication table of what value? '))
    if n < 0: 
        break
    for i in range(1,11):
        print(f'{color["cyan"]}{n} X {i:2} = {n * i} {color["clear"]}')
print(line)
print(f'{color["purple"]}Multiplication table program closed.{color["clear"]}')
