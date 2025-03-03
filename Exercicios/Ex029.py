vel = float(input('\033[1;33mQual e a velocidade atual do carro? '))
if vel > 80:
    print(f'\033[1;31mMULTADO! voce exedeu o limite de velocidade que era de 80km/h.')
    print(f'Voce deve pagar uma multa de \033[1;33mR${(vel-80)*7:.2f}!')
print('\033[1;33mTenha um bom dia! Dirija em segurança!\033[m')
