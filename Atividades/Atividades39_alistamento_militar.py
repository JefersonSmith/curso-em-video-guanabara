# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Em que ano você nasceu: '))
idade = 2023 - ano

print(f'Você tem {idade} anos')
if idade < 18:
    print(f'Faltam {18 - idade} ano(s) para você alistar')
elif idade == 18:
    print('Você deve se alistar esse ano')
else:
    print(f'Você deveria ter se alistado {idade - 18} ano(s) atrás')