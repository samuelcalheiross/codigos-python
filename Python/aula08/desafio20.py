import random

aluno1 = str(input('Nome do 1° aluno: '))
aluno2 = str(input('Nome do 2° aluno '))
aluno3 = str(input('Nome do 3° aluno: '))
aluno4 = str(input('Nome do 4° aluno: '))

nomes = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(nomes)#O shuffle não necessita ser armazenado em uma variável para funcionar

print(f'Primeira ordem sorteada: {random.sample(nomes, 2)}')
print(f'Segunda ordem sorteada: {nomes}')