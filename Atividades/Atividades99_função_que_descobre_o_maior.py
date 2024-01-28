# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que
# analisar todos os valores e dizer qual deles é o maior.

quant = int(input('Quantos valores você quer digitar?: '))


def maior(quant):
    max = 0
    informados = 0
    for i in range(quant):
        numero = int(input(f'Numero {i + 1}: '))
        if numero > max:
            max = numero
        informados += 1
    print(f'Foram informados {informados} números')
    print(f'O maior número informado foi {max}')


maior(quant)