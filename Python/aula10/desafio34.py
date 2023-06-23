salario = float(input('Digite o valor do seu salário: '))

if salario > 1250:
    print(f'Seu salário de R$ {salario}, passará a ser R$ {salario*1.1:.2f}')
else:
    print(f'Seu salário de R$ {salario} passará a ser R$ {salario*1.15:.2f}')