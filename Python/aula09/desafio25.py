#PRIMEIRO MÉTODO
nome = str(input('Digite seu nome: ')).upper()
resultado = nome.count('SILVA')

if resultado == 0:
    print('Seu nome não tem "Silva"')

else:
    print('Seu nome tem "Silva"')

#SEGUNDO MÉTODO
nome = input('Digite seu nome: ').upper()


result = bool(nome.count('SILVA'))

print(f'Seu nome possui "Silva"? {result}')

#TERCEIRO MÉTODO
nome = str(input('Digite Seu nome: '))

print(f'Seu nome tem "Silva? {"SILVA" in nome.upper()}"')
