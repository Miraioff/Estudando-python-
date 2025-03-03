print(f'\033[1;31m=-\033[m'*15)
print(f'\033[1;35mAnalisador de triangulos \033[m')
print(f'\033[1;31m=-\033[m'*15)
s1 = float(input('\033[1;35mPrimeiro segmento: \033[m'))
s2 = float(input('\033[1;35mSegundo segmento: \033[m'))
s3 = float(input('\033[1;35mTerceiro segmento: \033[m'))

if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    print(f'\033[1;35mOs segmentos acima \033[1;32mPODEM FORMAR um triangulo.\033[m')
else:
    print(f'\033[1;35mOs segmentos acima \033[1;31mNAO PODEM FORMAR um triangulo.\033[m')
