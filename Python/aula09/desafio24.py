cidade = str(input('Qual o nome da sua cidade? ')).strip().upper()

resultado = cidade.startswith('SANTO')

print(f'Sua cidade começa com "Santo"? {resultado}')
