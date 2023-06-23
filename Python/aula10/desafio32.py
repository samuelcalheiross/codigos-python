from datetime import date
ano = int(input('Digite o ano que deseja analisar. Coloque 0 para o ano atual. '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é Bissexto')
else:
    print(f'{ano} não é Bissexto')