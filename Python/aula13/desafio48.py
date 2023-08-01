#Quantidade e soma de números ímpares de 1 a 500
print('Números ímpares multiplos de três de 1 a 500:')

soma = 0
contador = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        contador += 1
print(f'A quantidade de números ímpares múltiplos de 3: {contador} \nSoma de todos esses números: {soma}')
