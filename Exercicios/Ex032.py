from datetime import date
from time import sleep 
ano = int(input('\033[1;35mQual ano voce quer analisar? Digite 0 para analisar o ano atual.\033[m'))
print('\033[1;35mANALISANDO...\033[m')
if ano == 0:
    ano = date.today().year
sleep(3)
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'\033[1;35mO ano {ano} e bissexto.\033[m')
else:
    print(f'\033[1;31mO ano {ano} nao e bissexto.\033[m')
    
