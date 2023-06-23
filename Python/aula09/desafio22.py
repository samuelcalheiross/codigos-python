nome = str(input('Digite seu nome completo: '))

print()
print(f'Seu nome com letras maiúsculas: {nome.upper()}')
print()
print(f'Seu nome com letras minúsculas: {nome.lower()}')

espacos = nome.replace(' ', '')

print()
print(f'Seu nome tem {len(espacos)} letras')
print()
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')