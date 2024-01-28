# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
maior = 0
menor = 0
for pessoas in range (1,8):
    nasc = int(input('E que ano a pessoa nasceu?: '))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
         menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E tivemos {menor} pessoas menores de idade')