from random import choice
alunos = [str(input('\033[1;35mDigite o nome do aluno: ')).strip(),
          str(input('Digite o nome do aluno: ')).strip(),
          str(input('Digite o nome do aluno: ')).strip(),
          str(input('Digite o nome do aluno: ')).strip()]
print(f'O aluno escolhido para apagar o quadro foi \033[1;31m{choice(alunos)}\033[m')

