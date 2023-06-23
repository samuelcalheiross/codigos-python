frase = str(input('Digite uma frase qualquer: ')).strip()

result = frase.upper().count('A')

if result == 1:
    print(f'A letra "a" aparece {result} vez')
else:
    print(f'A letra "a" aparece {result} vezes')


print(f'A letra "a" aparece pela primeira vez na posição {frase.upper().find("A")+1}')
print(f'A letra "a" aparece pela segunda vez na posição {frase.upper().rfind("A")+1}')
 