frase = str(input('\033[1;36mDigite uma frase: ')).strip().lower()
print(f'\033[1;35mA letra "A" aparece {frase.count('a')} vezes na frase.\033[m')
print(f'\033[1;35mA primeira letra "A" apareceu na posição {frase.find('a')+1}\033[m')
print(f'\033[1;35mA ultima letra "A" apareceu na posição {frase.rfind('a')+1}\033[m')
