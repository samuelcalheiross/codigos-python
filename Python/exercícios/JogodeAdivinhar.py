from random import randint
from time import sleep

print()
print('-+'*64)
print('BEM VINDO AO JOGO!')
print('Divirta-se competindo com seus amigos para ver quem é o melhor em adivinhar o número gerado pelo computador!')
print()
print('Selecione a dificuldade:')
print('[ 1 ] Fácil: Número gerado vai de 1 a 10\n[ 2 ] Médio: Número gerado vai de 1 a 50\n[ 3 ] Difícil: Número gerado vai de 1 a 100\n[ 4 ] Insano: Número gerado vai de 1 a 1000')
dificuldade = input('Digite: ')
print('-+'*64)

while dificuldade != '1' and dificuldade != '2' and dificuldade != '3' and dificuldade != '4':
    sleep(1/2)
    print()
    print('Opção inválida!')
    print()
    print('Selecione a dificuldade, novamente:')
    print('[ 1 ] Fácil: Número gerado vai de 1 a 10\n[ 2 ] Médio: Número gerado vai de 1 a 50\n[ 3 ] Difícil: Número gerado vai de 1 a 100\n[ 4 ] Insano: Número gerado vai de 1 a 1000')
    dificuldade = input('Digite: ').strip()

if dificuldade == '1':
    sleep(1/2)
    print()

    min_num = 1
    max_num = 10
    computador = randint(min_num, max_num)

    print('Vamos, lá...')
    chute = int(input('Chute um número de 1 a 10: '))

    while chute < 1 or chute > 10:
        chute = int(input('Chute um número de 1 a 10: '))

    if chute == computador:
        sleep(1/2)
        print('-'*32)
        print(f'Parabéns, você acertou! O número é {computador}')
        print()
        print('FIM DE JOGO')
        print('-+'*64)
    else:

        while chute != computador:
            if chute < computador:
                sleep(1/2)
                print('-'*32)
                print('Xiiii, chutou baixo!')
                print(f'O número está entre {chute} e {max_num}')
                print()
                min_num = chute
                chute = int(input('Chute, novamente: '))
            else:
                sleep(1/2)
                print('-'*32)
                print('Xiiii, chutou alto!')
                print(f'O número está entre {min_num} e {chute}')
                print()
                max_num = chute
                chute = int(input('Chute, novamente: '))
        if chute == computador:
            sleep(1/2)
            print('-'*32)
            print(f'Parabéns, você acertou! O número é {computador}')
            print()
            print('FIM DE JOGO')
            print('-+'*64)

elif dificuldade == '2':
    sleep(1/2)
    print()

    min_num = 1
    max_num = 50
    computador = randint(min_num, max_num)

    print('Vamos, lá...')
    chute = int(input('Chute um número de 1 a 50: '))

    while chute < 1 or chute > 50:
        chute = int(input('Chute um número de 1 a 50: '))

    if chute == computador:
        sleep(1/2)
        print('-'*32)
        print(f'Parabéns, você acertou! O número é {computador}')
        print()
        print('FIM DE JOGO')
        print('-+'*64)
    else:

        while chute != computador:
            if chute < computador:
                sleep(1/2)
                print('-'*32)
                print('Xiiii, chutou baixo!')
                print(f'O número está entre {chute} e {max_num}')
                print()
                min_num = chute
                chute = int(input('Chute, novamente: '))
            else:
                sleep(1/2)
                print('-'*32)
                print('Xiiii, chutou alto!')
                print(f'O número está entre {min_num} e {chute}')
                print()
                max_num = chute
                chute = int(input('Chute, novamente: '))
        if chute == computador:
            sleep(1/2)
            print('-'*32)
            print(f'Parabéns, você acertou! O número é {computador}')
            print()
            print('FIM DE JOGO')
            print('-+'*64)

elif dificuldade == '3':
    sleep(1/2)
    print()

    min_num = 1
    max_num = 100
    computador = randint(min_num, max_num)

    print('Vamos, lá...')
    chute = int(input('Chute um número de 1 a 100: '))

    while chute < 1 or chute > 100:
        chute = int(input('Chute um número de 1 a 100: '))

    if chute == computador:
        sleep(1/2)
        print('-'*32)
        print(f'Parabéns, você acertou! O número é {computador}')
        print()
        print('FIM DE JOGO')
        print('-+'*64)
    else:

        while chute != computador:
            if chute < computador:
                sleep(1/2)
                print('-'*32)
                print('Xiiii, chutou baixo!')
                print(f'O número está entre {chute} e {max_num}')
                print()
                min_num = chute
                chute = int(input('Chute, novamente: '))
            else:
                sleep(1/2)
                print('-'*32)
                print('Xiiii, chutou alto!')
                print(f'O número está entre {min_num} e {chute}')
                print()
                max_num = chute
                chute = int(input('Chute, novamente: '))
        if chute == computador:
            sleep(1/2)
            print('-'*32)
            print(f'Parabéns, você acertou! O número é {computador}')
            print()
            print('FIM DE JOGO')
            print('-+'*64)

elif dificuldade == '4':
    sleep(1/2)
    print()

    min_num = 1
    max_num = 1000
    computador = randint(min_num, max_num)

    print('Vamos, lá...')
    chute = int(input('Chute um número de 1 a 1000: '))
    while chute < 1 or chute > 1000:
        chute = int(input('Chute um número de 1 a 1000: '))

    if chute == computador:
        sleep(1/2)
        print('-'*32)
        print(f'Parabéns, você acertou! O número é {computador}')
        print()
        print('FIM DE JOGO')
        print('-+'*64)
    else:

        while chute != computador:
            if chute < computador:
                sleep(1/2)
                print('-'*32)
                print('Xiiii, chutou baixo!')
                print(f'O número está entre {chute} e {max_num}')
                print()
                min_num = chute
                chute = int(input('Chute, novamente: '))
            else:
                sleep(1/2)
                print('-'*32)
                print('Xiiii, chutou alto!')
                print(f'O número está entre {min_num} e {chute}')
                print()
                max_num = chute
                chute = int(input('Chute, novamente: '))
        if chute == computador:
            sleep(1/2)
            print('-'*32)
            print(f'Parabéns, você acertou! O número é {computador}')
            print()
            print('FIM DE JOGO')
            print('-+'*64)
