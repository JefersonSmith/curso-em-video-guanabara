# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# pessoas = []
# cadastradas = 0
# pesadas = ["", 0]
# leves = ["", 999]
#
# while True:
#     cadastradas += 1
#     pessoas.append([input('Qual o seu nome: '), int(input('Qual o seu peso?: '))])
#     continuar = input('Quer continuar? [S/N]: ')
#     if continuar in 'Nn':
#         break
#     if pessoas[0][1] > pesadas:
#         pesadas.append(pessoas)
#     if pessoas[0][1] < leves:
#         leves.append(pessoas)
#
# print(f'Foram cadastradas {cadastradas} pessoas')
# print(f'A pessoa mais pesada é {pesadas}')
# print(f'A pessoa mais leve é {leves}')

temp = []
princ = []
maior = 0
menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Os dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}Kg. Peso de  ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')