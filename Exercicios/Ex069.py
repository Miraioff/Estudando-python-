color = {
    'cyan' : '\033[1;36m',
    'clear' : '\033[m',
    'yellow' : '\033[1;33m'
}
line = f'{color["yellow"]}=-{color["clear"]}'*25
under20 = 0
more18 = 0
cont_male = 0
while True:
    print(line)
    print(f'{color["cyan"]}{"REGISTER A PERSON":^50}{color["clear"]}')
    print(line)
    while True:
        try:
            age = int(input(f'{color["cyan"]}Age: '))
            break
        except ValueError:
            print(f'{color["cyan"]}Invalid input! Please enter a valid number. {color["clear"]}')
    sex = ''
    sex = str(input(f'{color["cyan"]}Sex [M/F] : ')).strip().upper()[0]
    while sex not in ['M','F']:
        sex = str(input(f'{color["cyan"]}Sex [M/F]: ')).strip().upper()[0]
    cont = ''
    cont = str(input(f'{color["cyan"]}Do you want to continue? [Y/N]')) .strip().upper()[0]
    while cont not in ['Y','N']:
        cont = str(input(f'{color["cyan"]}Do you want to continue? [Y/N] ')).strip().upper()[0]

    if age >= 18:
        more18 += 1
    if sex == 'M':
        cont_male += 1
    if sex == 'F' and age < 20:
        under20 += 1
    
    if cont == 'N':
        break
print(line)
print(f'{color["cyan"]}{"END OF PROGRAM":^50}{color["clear"]}')
print(line)
print(f'{color["cyan"]}Total number of people over 18 years old: {more18}')
print(f'{color["cyan"]}There are  {cont_male} registered men in total. ')
print(f'{color["cyan"]}There are  {under20} women under the age  of 20.')
