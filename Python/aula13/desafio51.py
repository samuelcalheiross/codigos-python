#Progressão aritmética seuqencia de 10 números

termoInicial = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

termoFinal = termoInicial + 11

print(f'A PA com termo inicial "{termoInicial}" e razão "{razao}" é a seguinte: ')
for termos in range(termoInicial, termoFinal, razao):
    print(termos, end=' ')
