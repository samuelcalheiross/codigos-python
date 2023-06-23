km = float(input('Qual a quantidade de Km percorridos pelo carro? '))
dias = float(input('Quantos dias o cliente ficou com o carro? '))
preco = (dias * 60) + (km * 0.15)
print(f'O total que o cliente deverá pagar pelo aluguel será de R${preco:.2f}')
