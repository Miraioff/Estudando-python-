sal = float(input('Qual e o salario do funcionario R$:'))

cor = {'limpa' : '\033[m',
       'red' : '\033[1;31m',
       'verde' : '\033[1;32m'}

if sal > 1250:
#Quem ganha acima de R$1250 ganha um aumento de 10% no salario 
    aumento = sal + (sal * 0.10)
else:
#Quem ganha igual ou menor que R$1250 ganha um aumento de 15%
    aumento = sal + (sal * 0.15)
print(f'Quem ganhava {cor['red']}R${sal:.2f}{cor['limpa']} passa a ganhar {cor['verde']}R${aumento:.2f}{cor['limpa']}.')
