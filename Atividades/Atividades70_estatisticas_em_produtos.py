# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.


total = 0.00
mil = 0
barato = 99999999999999999999
mais_barato = ""
while True:
    produto = input('Qual o nome do produto?: ')
    valor = float(input('Qual o valor do produto?: '))
    total += valor
    if valor > 1000:
        mil += 1
    if valor < barato:
        barato = valor
        mais_barato = produto
    continuar = input('Quer continuar? [S/N]: ').upper()
    if continuar == 'N':
        break
print(f'O preço total da compra é {total}, {mil} produtos custam mais de R$ 1.000,00 e o produto mais barato é {mais_barato} que custa {barato}')
