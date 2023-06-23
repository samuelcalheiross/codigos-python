#MANEIRA QUE EU FIZ
print()
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num2 > num3:
    print()
    print(f'{num1} é o maior')

if num1 > num2 and num2 < num3:
    print()
    print(f'{num3} é o maior' if num3 > num1 else f'{num1} é o maior')

if num1 < num2 and num2 < num3:
    print()
    print(f'{num3} é o maior')

if num1 < num2 and num2 > num3:
    print()
    print(f'{num2} é o maior')

if num1 == num2 == num3:
    print()
    print('Os três números são iguais')

#CHAT GPT
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = num1  # Assume que o primeiro número é o maior

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

menor = num1

if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3


if num1 == num2 == num3:
    print('Os três números são iguais')
else:
    print(f'O maior número é {maior}')
    print(f'O menor número é {menor}')
