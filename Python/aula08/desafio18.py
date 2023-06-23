import math

valor = int(input('Digite um ângulo: '))
angulo_radians = math.radians(valor)

sen = math.sin(angulo_radians)
cos = math.cos(angulo_radians)
tan = math.tan(angulo_radians)

print('-' * 32)
print(f'O Seno de {valor} é {sen:.3f}')
print(f'O Cosseno de {valor} é {cos:.3f}')
print(f'A tangente de {valor} é {tan:.3f}')
print('-' * 32)