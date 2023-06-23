#forma em string (limitada)
'''num = str(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')'''

#forma matemática
num1 = int(input('Digite um número de 0 a 9999: '))
u = num1 // 1 % 10
d = num1 // 10 % 10
c = num1 //100 % 10
m = num1 // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')




