
nome = str(input('Seu nome: '))
if nome != nome.title():
    print('***Escreva seu nome utilizando maiúsculas no começo***')
    nome = str(input('Seu nome: '))
    print('Ok, nome confirmado!')
else:
    print('Ok, nome confirmado!')

nome = str(input('Agora, escreva seu nome em CAPSLOCK: '))
if nome != nome.upper():
    print('***Por favor, escreva seu nome com o CAPSLOCK ativado***')
    nome = str(input('Seu nome: '))
    print('Ok, nome confirmado!')
else:
    print('Ok, nome confirmado!')