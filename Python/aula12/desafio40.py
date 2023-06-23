nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if 0 < media < 5:
    print(f'Média {media:.1f}')
    print('Reprvado!')
elif 5 <= media <= 6.9:
    print(f'Média {media:.1f}')
    print('Recuperação!')
else:
    print(f'Média {media:.1f}')
    print('Aprovado!')
