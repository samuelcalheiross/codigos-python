# DE ACORDO COM A IDADE

idade = int(input('Digite sua idade: '))

if idade < 18:
    if idade == 17:
        print('Falta 1 ano para você se apresentar ao serviço militar.')
    else:
        print(
            f'Faltam {18 - idade} anos para você se apresentar ao serviço militar. ')
elif idade == 18:
    print('Você está na idade do alistamento militar!')
elif idade > 18:
    if idade == 19:
        print('Faz 1 ano desde o seu alistamento. Se não se alistou, compareça à junta militar mais próxima.')
    elif idade == 20:
        print('Faz 2 anos desde o seu alistamento. Se não se alistou, compareça à junta militar mais próxima.')
    else:
        print(f'Faz {idade - 18} anos desde o seu alistamento.')

# DE ACORDO COM O ANO DE NASCIMENTO
from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    print(f'Você tem {idade} anos')
    print(f'Falta {18 - idade} ano(s) para seu alistamento')
    print(f'Você deverá se alistar em {nascimento + 18}')
elif idade > 18:
    print(f'Você tem {idade} anos')
    print(f'Seu alistamento foi em {atual - (idade - 18)}')
    print(f'Caso você não tenha se alistado, já deveria ter feito há {idade - 18} ano(s)')
