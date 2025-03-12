frase = str(input('\033[1;35mDigite um frase: \033[m')).strip().lower()
# separa as palavras em lista
palavras = frase.split()
#ultiliza os espacos para juntar as palavras
junta = ''.join(palavras)
#ira invertar a frase sem espacos
inverso = ''
for letra in range(len(junta)-1,-1,-1):
    inverso += junta[letra]
print(f'\033[1;35mO inverso de \033[1;36m{junta} \033[1;35me \033[1;33m{inverso}.\033[m')
if junta == inverso:
    print(f'\033[1;32mTemos um palindromo!\033[m')
else:
    print(f'\033[1;31mNao temos um palindromo!\033[m')


