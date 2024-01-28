# Exercício Python 082: Crie um programa que vai ler vários números
# e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    numeros = int(input("Digite um número: "))
    lista.append(numeros)
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
    pergunta = input("Quer continuar? [S/N]: ")
    if pergunta in 'Nn':
        break

lista.sort()
pares.sort()
impares.sort()
print(f'Esses foram os valores digitados {lista}')
print(f'O valores pares são {pares}')
print((f'Os valores impares são {impares}'))