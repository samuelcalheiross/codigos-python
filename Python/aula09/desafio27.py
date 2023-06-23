#MÉTODO 1
nome = str(input('Digite seu nome completo: ')).strip()

divisao = nome.split()
print()
print(f'Muito prazer em te conhecer {nome}!')
print()
print(f'Seu último nome é {divisao[-1]}')
print(f'Seu primeiro nome é {divisao[0]}')

#MÉTODO 2
nome = str(input('Digite seu nome completo: ')).strip()

divisao = nome.split()
print()
print(f'Muito prazer em te conhecer, {nome}!')
print()
print(f'Seu último nome é {divisao[len(divisao)-1]}')
print(f'Seu primeiro nome é {divisao[0]}')
print()