# Exercício Python 085: Crie um programa onde o usuário possa
# digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

numero = [[],[]]

for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)

numero[0].sort
numero[1].sort
print(f'Todos os valores digitados: {numero}')
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores impares digitados foram: {numero[1]}')
