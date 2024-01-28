# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

ano = int(input('Em que ano você nasceu?: '))
idade = 2023 - ano

if idade < 10:
    print(f'Você tem {idade} anos e é da categoria MIRIM')
elif idade < 15:
    print(f'Você tem {idade} anos e é da categoria INFANTIL')
elif idade < 20:
    print(f'Você tem {idade} anos e é da categoria JÚNIOR')
elif idade < 26:
    print(f'Você tem {idade} anos e é da categoria SÊNIOR')
else:
     print(f'Você tem {idade} anos e é da categoria MASTER')