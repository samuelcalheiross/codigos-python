#CALCULADORA DE PREÇOS
preco1 = float(input('Digite o preço do primeiro produto: R$'))
preco2 = float(input('Digite o preço do segundo produto: R$'))
preco3 = float(input('Digite o preço do terceiro produto: R$'))

menor = preco1

if menor < preco2 and menor < preco3:
    print(f'Escolha o primeiro produto (R${preco1:.2f})')
elif preco2 < menor and preco2 < preco3:
    menor = preco2
    print(f'Escolha o segundo produto (R${preco2:.2f})')
else:
    menor = preco3
    print(f'Escolha o terceiro produto (R${preco3:.2f})')

#MOSTRANDO NÚMEROS EM ORDEM DECRESCENTE
print()
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

if maior == num1 and menor == num2:
    print(f'Ordem decrescente: {num1}, {num3}, {num2}')
elif maior == num1 and menor == num3:
    print(f'Ordem decrescente: {num1}, {num2}, {num3}')
elif maior == num2 and menor == num3:
    print(f'Ordem decrescente: {num2}, {num1}, {num3}')
elif maior == num2 and menor == num1:
    print(f'Ordem decrescente: {num2}, {num3}, {num1}')
elif maior == num3 and menor == num1:
    print(f'Ordem decrescente: {num3}, {num2}, {num1}')
elif maior == num3 and menor == num2:
    print(f'Ordem decrescente: {num3}, {num1}, {num2}')

# QUAL TURNO VC ESTUDA?
from time import sleep
print()
print('Em qual turno você estuda?')
print('[M] Matutino')
print('[V] Vespertino')
print('[N] Noturno')
turno = input('Digite: ').strip().lower()

sleep(1/2)

nome = input('Agora digite seu nome: ')
print('...')
sleep(1)

if turno == 'm':
    print(f'Bom dia, {nome}')
elif turno == 'v':
    print(f'Boa tarde, {nome}')
elif turno == 'n':
    print(f'Boa noite, {nome}')
else:
    print('Valor inválido!')

#REAJUSTES EM SALÁRIOS
print()
salario = float(input('Digite aqui o seu salário: R$ '))

if 0 < salario <= 280:
    print()
    print(f'Salário anterior: R$ {salario:.2f}')
    print('Percentual de aumento: 20%')
    print(f'Valor do aumento: R$ {(salario*1.2 - salario):.2f}')
    print(f'Salário atual: R$ {salario*1.2:.2f}')
elif 280 < salario <= 700:
    print()
    print(f'Salário anterior: R$ {salario:.2f}')
    print('Percentual de aumento: 15%')
    print(f'Valor do aumento: R$ {(salario*1.15 - salario):.2f}')
    print(f'Salário atual: R$ {salario*1.15:.2f}')
elif 700 < salario < 1500:
    print()
    print(f'Salário anterior: R$ {salario:.2f}')
    print('Percentual de aumento: 10%')
    print(f'Valor do aumento: R$ {(salario*1.1 - salario):.2f}')
    print(f'Salário atual: R$ {salario*1.1:.2f}')
elif salario >= 1500:
    print()
    print(f'Salário anterior: R$ {salario:.2f}')
    print('Percentual de aumento: 5%')
    print(f'Valor do aumento: R$ {(salario*1.05 - salario):.2f}')
    print(f'Salário atual: R$ {salario*1.05:.2f}')

#DIA DA SEMANA
num = int(input('Digite um número: '))

if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda')
elif num == 3:
    print('Terça')
elif num == 4:
    print('Quarta')
elif num == 5:
    print('Quinta')
elif num == 6:
    print('Sexta')
elif num == 7:
    print('Sábado')
else: 
    print('Valor inválido!')

# EQUAÇÃO DO SEGUNDO GRAU
import sys
a = float(input("Informe o valor de a: "))

if a == 0:
    print()
    print('A equação não é do segundo grau (TENTE NOVAMENTE)')
    print()
    sys.exit()
b = float(input("Informe o valor de b: "))
c = float(input("Infomre o valor de c: "))

delta = b**2 - 4 * a*c

if delta < 0:
    print()
    print('A equação apresentada não possui raizes reais')
    print()
elif delta == 0:
    print()
    print('A equação apresentada possui somente uma raiz real')
    print()
elif delta > 0:
    print()
    print('A equação apresentada possui duas raizes reais')

