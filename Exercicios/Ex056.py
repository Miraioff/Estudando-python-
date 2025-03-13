linha = f'\033[1;35m=-\033[m'*10
smedia = 0
soma_menor20 = 0
mais_velho = 0
nomevelho = ''
for p in range(1,5):
    print(linha)
    try:
        nome = str(input('Nome :')).strip().title()
        idade = int(input('Idade :'))
        sexo = str(input('Sexo[M/F] : ')).strip().upper()
        if idade <= 0 or sexo != 'M' and sexo != 'F':
            print(f'Entrada invalida!')
            exit()
    except ValueError:
        print('Entrada Invalida!')
    
    if sexo == 'F' and idade < 20:
        soma_menor20 += 1
    
    if p == 1 and sexo == 'M':
        mais_velho = idade
        nomevelho = nome
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nomevelho = nome

    smedia += idade
media_idade = smedia / 4
print(linha)
print(f'A media de idade do grupo e {media_idade:.1f}')
print(f'A idade do Homem mais velho e {mais_velho} anos e seu nome e {nomevelho}.')
print(f'{soma_menor20} mulheres tem menos que 20 anos.')
    
