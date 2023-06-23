num = int(input('Digite o número que deseja converter: '))
print()
print('Digite 1 para BINÁRIO.')
print('Digite 2 para OCTAL.')
print('Digite 3 para HEXADECIMAL.')
escolha = int(input('Número: '))

if escolha == 1:
    print()
    print(f'O número {num} em Binário é {bin(num)}')
elif escolha == 2:
    print()
    print(f'O número {num} em Octal é {oct(num)}')
elif escolha == 3:
    print()
    print(f'O número {num} em Hexadecimal é {hex(num)}')
else: 
    print()
    print('Número inválido!')