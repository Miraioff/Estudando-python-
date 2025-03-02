from random import sample
alunos = [str(input('\033[1;35mDigite o nome do primeiro aluno: ')).strip().title(),
          str(input('Digite o nome do segundo aluno: ')).strip().title(),
          str(input('Digite o nome do terceiro aluno: ')).strip().title(),
          str(input('Digite o nome do quarto aluno: ')).strip().title()]
print(f'A ordem para apresentacao do trabalho sera \033[1;36m{sample(alunos,k=4)}\033[m')
