val = float(input('\033[1;33mQual e o valor do produto?R$ \033[m'))
#calculo do desconto
desc = val - (val * 0.05)

cor = {'limpa' : '\033[m',
       'red' : '\033[4;31m',
       'verde' : '\033[1;32m'}

print(f'{cor['verde']}O produto que custa R${val:.2f}, Com 5% de desconto passara a custar R${desc:.2f}.{cor['limpa']}')
print(f'{cor['red']}Desconto recebido R${val*0.05:.2f} .{cor['limpa']}')