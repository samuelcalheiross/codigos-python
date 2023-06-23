num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
num5 = int(input('Número 5: '))
num6 = int(input('Número 6: '))

soma = 0
for numeros in range(num1, num6+1):
    if numeros % 2 == 0:
        soma += numeros
print(f'A soma dos números pares é {soma}')
