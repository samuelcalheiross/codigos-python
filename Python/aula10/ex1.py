#Ex1
nome = str(input('Digite seu nome: '))
if nome == 'Samuel':
    print(f'Que nome lindo você tem {nome}')
else:
    print(f'Bom dia, {nome}, seu nome é tão normal...')

#Ex2

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2

print()
print(f'Sua média foi {media}')
print()

if media >= 7:
    print('Parabéns, você foi aprovado!!')
    print()
else:
    print('Você foi reprovado, estude mais!!!')
    print()


