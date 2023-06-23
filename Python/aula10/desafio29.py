km = float(input('Velocidade do carro: '))

if km > 80:
    print()
    print('Você foi multado!')
    print(f'Sua multa será de R$ {(km - 80)*7:.2f}')
    print()
else: 
    print('Sua velocidade está dentro da normalidade.')