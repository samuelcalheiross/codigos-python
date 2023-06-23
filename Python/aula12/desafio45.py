from random import choice
from time import sleep
print()
print('-+'*64)
print('Vamos brincar de Jokenpô??')
print('-+'*64)

opcoes = ['pedra', 'papel', 'tesoura']
jogador = str(input('Escolha "pedra", "papel" ou "tesoura": '))
computador = choice(opcoes)
print()
print('JOKENPÔ...')
sleep(3)

if computador == 'papel'and jogador == 'papel':
    print()
    print(computador)
    print('EMPATE!')
elif computador == 'pedra' and jogador == 'pedra':
    print()
    print(computador)
    print('EMPATE!')
elif computador == 'tesoura' and jogador == 'tesoura':
    print()
    print(computador)
    print('EMPATE!')
elif computador == 'papel' and jogador == 'pedra':
    print()
    print(computador)
    print('EU GANHEI!')
elif computador == 'pedra' and jogador == 'papel':
    print()
    print(computador)
    print('VOCÊ GANHOU!')
elif computador == 'pedra' and jogador == 'tesoura':
    print()
    print(computador)
    print('EU GANHEI!')
elif computador == 'tesoura' and jogador == 'pedra':
    print()
    print(computador)
    print('VOCÊ GANHOU!')
elif computador == 'tesoura' and jogador == 'papel':
    print()
    print(computador)
    print('EU GANHEI!')
elif computador == 'papel' and jogador == 'tesoura':
    print()
    print(computador)
    print('VOCÊ GANHOU!')
else:
    print('Escolha inválida')
