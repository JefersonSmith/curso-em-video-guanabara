# Exercício Python 081:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    pergunta = input('Quer continuar [S/N]?: ')
    if pergunta in 'Nn':
        break

print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista digitada foi {lista}')
if 5 in lista:
    print('o valor 5 foi digitado')
else:
    print('Você não digitou o valor 5')