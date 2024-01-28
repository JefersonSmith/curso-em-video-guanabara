# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 1000

for i in range(1, 6):
    peso = int(input(f'Qual o peso da {i}ª pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso foi {maior}')
print(f'O menor peso foi {menor}')
