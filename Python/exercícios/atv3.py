#1
valor = float(input('Valor do produto: R$ '))
quantidade = int(input('Quantos produtos são? '))

valor_final = valor * quantidade

if quantidade >= 10:
    print('Valor final (10 por cento de desconto): ')
    print(f'R$ {valor_final * 0.9:.2f}')
else:
    print('Valor final:')
    print(f'R$ {valor_final:.2f}')

#2
media = float(input('Digite a média final: '))

if media < 5:
    print('Sua média está no Conceito "D"')
elif 5 <= media < 7:
    print('Sua média está no Conceito "C"')
elif 7 <= media < 9:
    print('Sua média está no Conceito "B"')
elif media >= 9:
    print('Sua média está no Conceito "A"')

#3
palavra1 = input('Digite uma palavra: ').lower().strip()
palavra2 = input('Digite outra palavra: ').lower().strip()

if len(palavra1) == len(palavra2):
    if sorted(palavra1) == sorted(palavra2):
        print(f'"{palavra1}" e "{palavra2}" são anagramas')
    else:
        print(f'"{palavra1}" e "{palavra2}" não são anagramas')
else:
    print(f'"{palavra1}" e "{palavra2}" não são anagramas')

#4
ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print(f'{ano} é bissexto')
elif ano % 100 == 0 and ano % 400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
