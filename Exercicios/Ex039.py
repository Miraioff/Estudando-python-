from datetime import date
color = {'clean' : '\033[m',
         'cyan' : '\033[1;36m',
         'red' : '\033[1;31m',
         'yellow' : '\033[1;33m'}
linha = f'{color['yellow']}=-{color['clean']}'*23
print(linha)
print(f'{color['cyan']}{"MILITARY DRAFT":^46}{color['clean']}')
print(linha)
try:
    sex = str(input(f'{color['cyan']}Please enter your gender: [Male/Female] {color['clean']}')).strip().title()
    if sex == 'Female':
        print(f'{color['yellow']}You do not need to do mandatory military enlistment.{color['clean']}')
        exit()
    elif sex == 'Male':
        y = int(input(f'{color['cyan']}Year of birth: {color['clean']}'))
        if y <= 0:
            print(f'{color['red']}invalid value!{color['clean']}')
            exit()
    else:
        print(f'{color['red']}Invalid input! Please enter "Male" or "Female"{color['clean']}')
        exit()
except ValueError:
        print(f'{color['red']}Invalid value! enter a year!{color['clean']}')
        exit()
print(linha)
age = date.today().year - y

print(f'{color['cyan']}People born in {y} are {age} years old in {date.today().year}.{color['clean']}')

if age < 18:
    print(f'{color['cyan']}there are still {18 - age} years left unitil enlistment.{color['clean']}')
    print(f'{color['cyan']}your enlistment will be in {y + 18}.{color['clean']}')
elif age > 18:
    print(f'{color['cyan']}you should have enlisted {age - 18} years ago.{color['clean']}')
    print(f'{color['cyan']}your enlistment was in{date.today().year - (age - 18)}{color['clean']}')
else:
    print(f'{color['cyan']}you have to enlist IMMEDIATELY.{color['clean']}')
print(linha)
