termo_inicial = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

termo_final = termo_inicial + 11

print(f'A PA com termo inicial "{termo_inicial}" e razão "{razao}" é a seguinte: ')
for termos in range(termo_inicial, termo_final, razao):
    print(termos, end=' ')
