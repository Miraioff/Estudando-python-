color = {
    'red' : '\033[1;31m',
    'clear' : '\033[m',
    'yellow' : '\033[1;33m',
    'purple' : '\033[1;35m'
}
line = f'{color["yellow"]}=-{color["clear"]}'*20
print(line)
print(f'{color["purple"]}{"SHOP":^40}{color["clear"]}')
total = 0
more1k = 0
cheaper = c = 0
name = ''
while True:
    print(line)
    while True:
        item = str(input(f'{color["purple"]}Product name: ')).strip().title()
        if item and not item.isdigit():
            break
        print(f'{color["red"]}Invalid input! Please enter a valid name. {color["clear"]}')

    while True:
        try:
            value = float(input(f'{color["purple"]}Price: R$'))
            break
        except ValueError:
            print(f'{color["red"]}Invalid input! Please enter a valid number.{color["clear"]}')
    while True:
        cont = str(input(f'{color["purple"]}Do you want to continue? [Y/N]')).strip().upper()
        if cont and cont[0] in ['Y', 'N']:
            cont = cont[0]
            break
        cont = str(input(f'{color["purple"]}Do you want to continue? [Y/N]')).strip().upper()[0]
    
    total += value

    if value > 1000:
        more1k += 1
    c += 1
    if c == 1 or value < cheaper:
        cheaper = value
        name = item

    if cont == 'N':
        break
print(line)
print(f'{color["purple"]}{"END PROGRAM":^40}{color["clear"]}')
print(line)
print(f'{color["purple"]}The purchase amount R${total:.2f}')
print(f'{color["purple"]}Number of products costing more than R$1000.00: {more1k}')
print(f'{color["purple"]}The cheapest product was {name}, costing R${cheaper:.2f}')
print(line)
