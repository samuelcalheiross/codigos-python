num = int(input('Digite um número: '))
print('-'*20)
print(f'Tabuada do {num}:')
print('-'*20)
for tabuada in range(0,11):
    print(f'{num} x {tabuada} = {tabuada*num}')
print('-'*20)
