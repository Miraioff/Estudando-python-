line = f'\033[1;33m-=\033[m'*25

print(line)
print(f'\033[1;36m{"PA GENERATOR":^50}')
print(line)

first = int(input(f'\033[1;36mFirst term: '))
reason = int(input(f'reason: '))
term = first
c = 1
while c <= 10:
    print(f'\033[1;32m{term}', end='\033[1;35m -> \033[m')
    #Update the term by adding the ratio
    term += reason
    c += 1
print(f'\033[1;32mEND\033[m')
# Displyas the first 10 terms os an PA