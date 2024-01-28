# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print (f'Você escolheu o número {numero} e ele é um número PAR')
else:
    print (f'Você escolheu o número {numero} e ele é um número ÍMPAR')