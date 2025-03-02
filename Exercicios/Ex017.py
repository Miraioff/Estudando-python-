from math import hypot
o = float(input('Informe o comprimento do \033[1;31mCATETO OPOSTO\033[m: '))
a = float(input('Informe o comprimento do \033[1;34mCATETO ADJACENTE\033[m: '))
print(f'O comprimento da hipotenusa sera \033[1;32m{hypot(o,a):.1f}\033[m')
