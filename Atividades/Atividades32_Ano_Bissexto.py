# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Quantos um ano?: '))

if ano % 4 == 0:
    print('Estamos em um ano Bissexto')
else:
    print('Não estamos em um ano Bissexto')