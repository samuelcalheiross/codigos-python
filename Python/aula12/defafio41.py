idade = int(input('Digite a idade do atleta: '))

if 0 < idade <= 9:
    print('CATEGORIA MIRIM')
elif 10 <= idade <= 14:
    print('CATEGORIA INFANTIL')
elif 15 <= idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade == 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
