n = int(input('Digite um numero: '))
print(f'Calculando {n}! =',end=' ')
c = n
f = 1
for c in range(n,0,-1):
    print(f'{c}',end=' ')
    if c > 1:
        print(f'x',end=' ')
    else:
        print(f'=',end=' ')
    f *= c
print(f, end=' ')
