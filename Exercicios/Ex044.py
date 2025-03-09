cor = {'roxo' : '\033[1;35m',
       'red' : '\033[1;31m',
       'amarelo' : '\033[1;33m',
       'limpa' : '\033[m',
       'cyan' : '\033[1;36m',
       'blue' : '\033[1;34m',
       'verde' : '\033[1;32m',
       'erro' : '\033[4;31m'}
lin = f'{cor["amarelo"]}=-{cor["limpa"]}'*25
print(lin)
print(f'{cor['roxo']}{"GERENCIADOR DE PAGAMENTO":^50}{cor['limpa']}')
print(lin)
try:
    valor = float(input(f'{cor['roxo']}Valor do produto R$: {cor['limpa']}'))
    pag = int(input(f'{cor['roxo']}Escolha a forma de pagamento\n'
                    f'1 para A VISTA com DINHEIRO/CHEQUE\n'
                    f'2 para A VISTA com CARTAO\n'
                    f'3 PARA ate 2x com CARTAO\n'
                    f'4 para 3x ou MAIS com CARTAO\n'
                    f'{cor['limpa']}'))
    if valor <= 0 or pag != 1 and pag != 2 and pag != 3 and pag != 4:
        print(f'{cor['erro']}Entrada Invalida{cor['limpa']}')
        exit()
except ValueError:
    print(f'{cor['erro']}Entrada Invalida!{cor['limpa']}')
    exit()
print(lin)
print(f'{cor['roxo']}O valor do produto e R${valor:.2f}\n'
      f'E voce escolheu a opcao {pag} para fazer o pagamento.{cor['limpa']}')
print(lin)
if pag == 1:
    valor_final = valor - (valor * 0.10)
    print(f'{cor['verde']}Voce recebeu 10% de desconto por pagar a vista no DINHEIRO/CHEQUE{cor['limpa']}')
    print(f'{cor['verde']}Voce pagara R${valor_final:.2f}{cor['limpa']}')
elif pag == 2:
    valor_final = valor - (valor * 0.05)
    print(f'{cor['cyan']}Voce recebeu 5% de desconto por pagar a vista no CARTAO.{cor['limpa']}')
    print(f'{cor['cyan']}Voce pagara R${valor_final:.2f}{cor['limpa']}')
elif pag == 3:
    parcelas = valor / 2
    print(f'{cor['blue']}Voce pagara o valor integral sem juros ou descontos.{cor['limpa']}')
    print(f'{cor['blue']}Voce pagara 2x de R${parcelas:.2f} no CARTAO.{cor['limpa']}')
else:
    valor_final = valor + (valor * 0.20)
    total_par = int(input(f'{cor['roxo']}Em quantas parcelas? {cor['limpa']}'))
    parcelas = valor_final / total_par
    print(f'{cor['red']}Voce devera pagar 20% de juros.{cor['limpa']}')
    print(f'{cor['red']}Voce pagara no total R${valor_final:.2f}')
    print(f'{cor['red']}Em {total_par}x de R${parcelas:.2f} no CARTAO.{cor['limpa']}')
