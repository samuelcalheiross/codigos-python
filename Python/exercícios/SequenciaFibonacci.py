'''Crie um programa que primeiramente solicite ao usuário a quantidade de números que ele 
deseja para um determinado conjunto. A partir disso, seu programa deve gerar essa quantidade 
de números utilizando a sequência de Fibonacci e salvar os números no conjunto. Após isso, 
seu programa deverá exibir em forma de fração NUMERADOR/DENOMINADOR, onde o numerador serão apenas
 os números PARES iniciando em 2 até o último número par de acordo com a quantidade de números 
 guardadas no conjunto inicial, e o denominador será cada número do conjunto inicial.'''

def fibo(n):
    sequencia = [0,1]
    while len(sequencia) < n:
        proximoNumero = sequencia[-1] + sequencia [-2]
        sequencia.append(proximoNumero)
    return sequencia

n = int(input('Quantos números deseja que a sequência fibonacci tenha? '))

conjunto = fibo(n)
numeradorPar = 2
print('Frações:')

for i in range(0, len(conjunto)):
    print(f'{numeradorPar}/{conjunto[i]}')
    numeradorPar += 2