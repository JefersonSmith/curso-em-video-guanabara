# Exercício Python 100: Faça um programa que tenha uma lista chamada
# números e duas funções chamadas sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista: ', end=' ')
    for i in range(5):
        sorteio = randint(0, 10)
        numeros.append(sorteio)
    for i in numeros:
        print(i, end=' ')
        sleep(.3)
    print('Pronto!')


def soma_par():
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'A soma dos valores pares de {numeros} é {soma}')


numeros = []
sorteia()
soma_par()
