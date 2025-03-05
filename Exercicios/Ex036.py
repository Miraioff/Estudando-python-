from time import sleep
linha = '\033[1;33m=-\033[m'*30
print(linha)
print(f' \033[1;35m{"VERIFICADOR DE EMPRESTIMO":^60}\033[m ')
print(linha)
print('\033[7;31mATENCAO: O EMPRESTIMO SERA NEGADO\n'
      'CASO A PRESTACAO MENSAL EXEDA OS 30% DO SEU SALARIO.\033[m')
print(linha)
# verifica se os valores da entrada sao numero e se sao positivos
try:
    casa = float(input('\033[1;35mInforme o valor da casa que deseja comprar R$:\033[m'))
    sal = float(input('\033[1;35mInforme o salario mensal do comprador R$:\033[m'))
    ano = int(input('\033[1;35mInforme em quantos anos deseja pagar sua casa: \033[m'))
    if casa <= 0 or sal <= 0 or ano <= 0:
        print('\033[1;31mOs valores devem ser positivos, Tente novamente!\033[m')
        exit()
except ValueError:
    print('\033[1;31mEntrada invalida!Digite apenas numero.\033[m')
    exit()

print('\033[1;35mVERIFICANDO INFORMACOES...\033[m')
sleep(2)
print(linha)
#calculo da prestacao mensal
pres_mensal = casa / (ano * 12)
#calculo dos 30% do salario 
terco = sal * 0.30
#verifica se a prestacao mensal exede os 30% do salario do comprador.
#se exerder  retorna o emprestimo negado, caso o contrario retorna as informacoes de compra
if pres_mensal <= terco:
    print(f'\033[1;32mParabens! Seu emprestimo foi APROVADO!\n'
          f'O valor da casa R${casa:.2f} .\n'
          f'Duracao: {ano} anos ({12*ano}meses).\n'
          f'Voce pagara um valor de R${pres_mensal:.2f}\033[m')
else:
    print(f'\033[1;31mO valor da prestacao mensal exedeu os 30% do seu salario.\n' 
           'Portanto seu emprestimo foi NEGADO!\033[m')
print(linha)
