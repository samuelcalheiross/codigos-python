print()
preco = float(input('Digite o valor normal do prouduto: R$'))
print('-' * 64)
print('Qual a sua condição de pagamento?')
print("Digite 1: À vista (dinheiro/cheque): 10 por cento de desconto.")
print('Digite 2: À vista (cartão): 5 por cento de desconto.')
print('Digite 3: Até 2x no cartão: preço normal.')
print('Digite 4: 3x ou mais no cartão: 20 por cento de juros.')
print('-' * 64)
escolha = int(input('Digite 1, 2, 3 ou 4: '))

if escolha == 1:
    print()
    print(f'Valor final (10% de desconto): R$ {preco*0.9:.2f}')
elif escolha == 2:
    print()
    print(f'Valor final (5% de desconto): {preco*0.95:.2f}')
elif escolha == 3:
    print()
    print('Você parcelou em 2x')
    print(f'Valor final (preço normal): R$ {preco/2:.2f}')
elif escolha == 4:
    print()
    print('Sua opção terá 20 por cento de juros por parcela.')
    escolha2 = int(input(f'Em quantas vezes deseja parcelar o valor de R${preco:.2f}? '))
    if 2 <= escolha2 <= 50:
        print()
        print(f'Você parcelou em {escolha2} vezes.')
        print(f'Valor mensal: R$ {(preco/escolha2)*1.2:.2f}')
    else:
        print('Número de parcelas inválido!')
else:
    print()
    print('Opção inválida de pagamento! Tente novamente.')
    