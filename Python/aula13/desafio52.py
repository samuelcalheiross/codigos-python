num = int(input('Digite um número inteiro: '))

if num == 1:
    print(f'{num} é primo')
else:
    for primos in range(num-1, 1, -1):
        if num % primos == 0:
            print(f'{num} não é primo')
            break
    else:
        print(f'{num} é primo')
