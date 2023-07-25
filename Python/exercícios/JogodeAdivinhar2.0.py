from random import randint
from time import sleep


def obter_dificuldade():
    print()
    print('-+'*64)
    print('BEM VINDO AO JOGO!')
    print('Divirta-se competindo com seus amigos para ver quem é o melhor em adivinhar o número gerado pelo computador!')
    print()
    print('Selecione a dificuldade:')
    print('[ 1 ] Fácil: Número gerado vai de 1 a 10\n[ 2 ] Médio: Número gerado vai de 1 a 50\n[ 3 ] Difícil: Número gerado vai de 1 a 100\n[ 4 ] Insano: Número gerado vai de 1 a 1000')

    while True:
        dificuldade = input('Digite: ').strip()
        if dificuldade in ['1', '2', '3', '4']:
            break
        else:
            sleep(1/2)
            print()
            print('Opção inválida!')
            print()
            print('Selecione a dificuldade, novamente:')
            print('[ 1 ] Fácil: Número gerado vai de 1 a 10\n[ 2 ] Médio: Número gerado vai de 1 a 50\n[ 3 ] Difícil: Número gerado vai de 1 a 100\n[ 4 ] Insano: Número gerado vai de 1 a 1000')
    print('-+'*64)
    return dificuldade


def obter_limites(dificuldade):
    if dificuldade == '1':
        return 1, 10
    elif dificuldade == '2':
        return 1, 50
    elif dificuldade == '3':
        return 1, 100
    elif dificuldade == '4':
        return 1, 1000


def gerar_numero_aleatorio(min_num, max_num):
    return randint(min_num, max_num)


def jogar_adivinhacao():
    dificuldade = obter_dificuldade()
    min_num, max_num = obter_limites(dificuldade)
    computador = gerar_numero_aleatorio(min_num, max_num)

    sleep(1/2)
    print(f'Vamos, lá... O número está entre {min_num} e {max_num}')

    while True:
        sleep(1/2)
        chute = int(input(f'Chute um número de {min_num} a {max_num}: '))
        if chute < min_num or chute > max_num:
            continue
        elif chute == computador:
            sleep(1/2)
            print(f'Parabéns, você acertou! O número é {computador}')
            print('FIM DE JOGO')
            break
        elif chute < computador:
            sleep(1/2)
            print('Xiiii, chutou baixo!')
            min_num = chute
        else:
            sleep(1/2)
            print('Xiiii, chutou alto!')
            max_num = chute


try:
    jogar_adivinhacao()
except ValueError:
    print('Ops, parece que você digitou um valor inválido. Por favor, reinicie o programa!')
except NameError:
    print('Ops, ocorreu um erro de digitação. Por favor, reinicie o programa!')
except KeyboardInterrupt:
    print('O programa foi interrompido!')
except Exception as erro:
    print(f'Ouve um problema inesperado: {erro}')
