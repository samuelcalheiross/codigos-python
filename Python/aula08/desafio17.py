import math

oposto = int(input('Cateto Oposto do triângulo: '))
adjascente = int(input('Cateto Adjascente do triângulo: '))
hipotenusa = math.pow(oposto, 2) + math.pow(adjascente, 2)
result = math.sqrt(hipotenusa)

print(f'O valor da Hipotenusa do triângulo retângulo de catetos {oposto} e {adjascente} será de {result}')
