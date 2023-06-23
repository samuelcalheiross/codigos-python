distancia = float(input('Digite a distância da sua viagem em Km: '))

if distancia > 200:
    print(f'O preço da sua viagem será de: R$ {distancia*0.45:.2f}')
else: 
    print(f'O preço da sua viagem será de {distancia*0.5:.2f}')
