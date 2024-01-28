# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))

divisor = 0

for i in range(1, numero+1):
    if numero % i == 0:
        divisor += 1
if divisor > 2:
    print("Não é primo")
else:
    print('É primo')