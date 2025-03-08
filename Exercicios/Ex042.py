cor = {'roxo' : '\033[1;35m',
       'red' : '\033[1;31m',
       'amarelo' : '\033[1;33m',
       'limpa' : '\033[m',
       'cyan' : '\033[1;36m',
       'blue' : '\033[1;34m',
       'verde' : '\033[1;32m'}
lin = f'{cor["amarelo"]}=-{cor['limpa']}'*30
print(lin)
print(f'{cor['roxo']}{"ANALISADOR DE TRIANGULOS":^60}{cor['limpa']}')
print(lin)
try:
    s1 = float(input(f'{cor['roxo']}Segmento 1: {cor['limpa']}'))
    s2 = float(input(f'{cor['roxo']}Segmento 2: {cor['limpa']}'))
    s3 = float(input(f'{cor['roxo']}Segmento 3: {cor['limpa']}'))
    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        print(f'{cor['red']}Entrada invalida!{cor['limpa']}')
        exit()
except ValueError:
    print(f'{cor['red']}Entrada invalida!{cor['limpa']}')
    exit()
print(lin)
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print(f'{cor['roxo']}Os segmentos PODEM formar um triangulo{cor['limpa']}')
    if s1 == s2 and s2 == s3:
        print(f'{cor['cyan']}Triangulo EQUILATERO.{cor['limpa']}')
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print(f'{cor['verde']}Triangulo ESCALENO.{cor['limpa']}')
    else:
        print(f'{cor['blue']}Triangulo ISOSCELES.{cor['limpa']}')
else:
    print(f'{cor['red']}Os segmentos acima NAO PODEM formar um triangulo.{cor['limpa']}')
print(lin)
