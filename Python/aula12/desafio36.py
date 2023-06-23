casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = float(input('Em quantos anos a casa será quitada? '))

prestacao = casa / (anos*12)

if prestacao > salario*0.3:
    print(f'Empréstimo negado! Sua prestação de R$ {prestacao:.2f} excedeu 30% do seu salário.')
else:
    print(f'Empréstimo permitido! Sua prestação ficou em R$ {prestacao:.2f} mensais.')

