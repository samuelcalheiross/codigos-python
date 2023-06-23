frase = input('Digite uma frase: ').strip().lower().replace(' ','')

tamanho = len(frase)
invertida = ''

for palindromo in range(tamanho-1, -1, -1):
    invertida += frase[palindromo]

if frase ==  invertida:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
