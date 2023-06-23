# ex1
distancia = float(input('Digite a distância da entrega em quilômetros: '))
if distancia > 500:
    print('A entrega deve ser feita por trasporte aéreo.')
else:
    print('A entrega deve ser feita por transporte terrestre.')

# ex2
preco = float(input('Digite o preço original do produto: '))
percentual = float(input('Digite o percentual de desconto: '))
if 0 > percentual > 100:
    print()
    print('PERCENTUAL INVÁLIDO!')
else:
    print(
        f'O valor final da compra é R${preco - (preco * percentual/100):.2f}')

# ex3
idade = str(input('Digite sua data de nascimento (formato: dd/mm/aaaa): '))
if int(idade[6:10]) > 2007:
    print()
    print('-' * 64)
    print('Desculpe, você não tem idade suficiente para jogar este jogo.')
    print('-' * 64)
else:
    print()
    print('-' * 64)
    print('Bem vindo(a), você tem idade suficiente para jogar!')

# ex4
print()
salario = float(input('Informe o salário bruto do funcionário: '))

if salario <= 1320:
    print()
    print('De acordo com o ano de 2023, o funcionário pagará:')
    print(f'-> 7,5% de INSS, que equivale a -R$ {salario*0.075:.2f}')
    print('-> 0% de IRPF, que equivale a -R$ 0.00')
    print('-' * 64)
    print(f'Salário líquido será de: R${salario - salario*0.075:.2f} ')
elif 1320.01 <= salario <= 2112:
    print()
    print('De acordo com o ano de 2023, o funcionário pagará:')
    print(f'-> 9,0% de INSS, que equivale a -R$ {salario*0.09:.2f}')
    print('-> 0% de IRPF, que equivale a -R$ 0.00')
    print('-' * 64)
    print(f'Salário líquido será de: R${salario - salario*0.09:.2f} ')
elif 2112.01 <= salario <= 2571.29:
    print()
    print('De acordo com o ano de 2023, o funcionário pagará:')
    print(f'-> 9,0% de INSS, que equivale a -R$ {salario*0.09:.2f}')
    print(f'-> 7,5% de IRPF, que equivale a -R$ {salario*0.075:.2f} ')
    print('-' * 64)
    print(f'Salário líquido será de: R${salario - salario*0.165:.2f} ')
elif 2571.30 <= salario <= 2826.65:
    print()
    print('De acordo com o ano de 2023, o funcionário pagará:')
    print(f'-> 12,0% de INSS, que equivale a -R$ {salario*0.12:.2f}')
    print(f'-> 7,5% de IRPF, que equivale a -R$ {salario*0.075:.2f} ')
    print('-' * 64)
    print(f'Salário líquido será de: R${salario - salario*0.195:.2f} ')
elif 2826.66 <= salario <= 3856.94:
    print()
    print('De acordo com o ano de 2023, o funcionário pagará:')
    print(f'-> 12,0% de INSS, que equivale a -R$ {salario*0.12:.2f}')
    print(f'-> 15,0% de IRPF, que equivale a -R$ {salario*0.15:.2f} ')
    print('-' * 64)
    print(f'Salário líquido será de: R${salario - salario*0.27:.2f} ')
elif 3856.95 <= salario <= 3751.05:
    print()
    print('De acordo com o ano de 2023, o funcionário pagará:')
    print(f'-> 14,0% de INSS, que equivale a -R$ {salario*0.14:.2f}')
    print(f'-> 15,0% de IRPF, que equivale a -R$ {salario*0.15:.2f} ')
    print('-' * 64)
    print(f'Salário líquido será de: R${salario - salario*0.29:.2f} ')
elif 3751.06 <= salario <= 4664.68:
    print()
    print('De acordo com o ano de 2023, o funcionário pagará:')
    print(f'-> 14,0% de INSS, que equivale a -R$ {salario*0.14:.2f}')
    print(f'-> 22,5% de IRPF, que equivale a -R$ {salario*0.225:.2f} ')
    print('-' * 64)
    print(f'Salário líquido será de: R${salario - salario*0.365:.2f} ')
elif 4664.68 <= salario <= 7507.49:
    print()
    print('De acordo com o ano de 2023, o funcionário pagará:')
    print(f'-> 14,0% de INSS, que equivale a -R$ {salario*0.14:.2f}')
    print(f'-> 27,5% de IRPF, que equivale a -R$ {salario*0.275:.2f} ')
    print('-' * 64)
    print(f'Salário líquido será de: R${salario - salario*0.415:.2f}'
          )
elif salario > 7507.49:
    print()
    print('De acordo com o ano de 2023, o funcionário pagará:')
    print(f'-> 14,0% de INSS, que equivale a -R$ {salario*0.14:.2f}')
    print(f'-> 27,5% de IRPF, que equivale a -R$ {salario*0.275:.2f} ')
    print('-' * 64)
    print(f'Salário líquido será de: R${salario - salario*0.415:.2f}')

# ex5
num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)

    if num < 2:
        print('O número não é primo.')
    else:
        primo = True

        for a in range(2, num):
            if num % a == 0:
                primo = False
                break

        if primo:
            print('O número é primo.')
        else:
            print('O número não é primo.')
else:
    print('Erro: O valor digitado não é um número inteiro.')

# ex6
salario = float(input('Digite o valor do salário mensal: R$'))
emprestimo = float(input('Digite o valor do empréstimo desejado: R$'))
idade = int(input('Digite a idade do cliente: '))

if salario < 2000:
    print(f'Empréstimo de R${emprestimo} reprovado!')
elif emprestimo > salario * 10:
    print(f'Empréstimo de R${emprestimo} reprovado!')
elif idade < 18 or idade > 65:
    print(f'Empréstimo de R${emprestimo} reprovado!')
else:
    print(f'Empréstimo de R${emprestimo} aprovado!')

# ex7
valor = float(input('Insira o valor da compra: R$'))

if valor >= 100 and valor < 200:
    print(
        f'O desconto a ser aplicado é de 10%. Valor total com desconto: R$ {valor*0.9:.2f}')
elif valor >= 200 and valor < 500:
    print(
        f' desconto a ser aplicado é de 20%. Valor total com desconto: R$ {valor*0.8:.2f}')
elif valor >= 500:
    print(
        f' desconto a ser aplicado é de 30%. Valor total com desconto: R$ {valor*0.7:.2f}')
elif valor < 100 and valor > 0:
    print(
        f'Não foi aplicada nenhuma regra de desconto. Valor total a pagar: R$ {valor}')
else:
    print('Valor de compra inválido!')
