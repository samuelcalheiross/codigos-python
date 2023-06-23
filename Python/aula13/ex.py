# 1
'''inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for a in range(inicio, fim+1, passo):
    print(a)
#2
nome = input('Informe seu nome: ')
print(f'Seu nome tem {len(nome)} letras. São elas: ')

for letra in nome:
    print(f'{letra}', end=" ")

#3
nome = input('Digite seu nome: ')
print(f'Seu nome tem {len(nome)} letras')

separador = " - "

for contador in range(0, len(nome)):
    if contador == len(nome)-1:
        separador = ""
    print(f'{nome[contador]}', end=separador)
#4
nome = 'samuel'
separador = " - "

for contador in range(len(nome)-1, -1, -1):
  if contador == 0:
    separador = ""
  print(f'{nome[contador]}', end=separador)'''

# 5
for a in range(1, 10+1):
    print(a)
print()
for a in range(0, 21, 2):
    print(a)
print()
for a in range(0, 101):
    print(a)
