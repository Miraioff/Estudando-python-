sal = float(input('\033[1;32mInforme o salario do funcionario: R$ '))
#calculo do salario + o aumento de 15% que ele ira receber
novo_sal = sal + (sal * 0.15)
cor = {'limpa' : '\033[m',
       'amarelo' : '\033[4;33m',
       'verde' : '\033[1;32m'}

print(f'{cor['verde']}O funcionario que recebe R${sal:.2f}, Com 15% de aumento ira passar  a receber R${novo_sal:.2f}{cor['limpa']}')
print(f'{cor['amarelo']}O aumento sera de R${sal*0.15:.2f}{cor['limpa']}')
