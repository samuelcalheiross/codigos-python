peso = float(input('Insira seu peso (Kg): '))
altura = float(input('Insira sua altura (metros): '))

imc = peso / altura**2

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Peso ideal')
elif 25 < imc <= 30:
    print('Acima do peso')
elif 30 < imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')