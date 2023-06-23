from random import randint
from time import sleep
num = int(input('Chute um número de 0 a 5: '))

chute = randint(0, 5)
print()
print('PROCESSANDO...')
sleep(1.5)
print()

if num == chute:
    print('Parabéns, você acertou!')
else: 
    print(f'Você errou! O número sorteado foi {chute}')
    