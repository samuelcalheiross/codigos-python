import random

aluno1 = str(input('Nome do 1° aluno(a): '))
aluno2 = str(input('Nome do 2° aluno(a): '))
aluno3 = str(input('Nome do 3° aluno(a): '))
aluno4 = str(input('Nome do 4° aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(alunos)

print(f'O aluno(a) sorteado foi: {sorteio}')