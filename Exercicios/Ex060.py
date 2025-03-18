n = int(input(f'Digite um numero: '))
c = n
f = 1
print(f'Calculando... {n}! =', end=' ')
while c > 0:    
   print(f'{c}',end=' ',)  
   if c == 1:
        print('=',end=' ') 
   else:
        print('x',end=' ')     
   f *= c
   c -= 1
print(f)
   




