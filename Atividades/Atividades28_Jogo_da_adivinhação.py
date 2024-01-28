# Exercício Python 28: Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero = random.randrange(0, 6)

escolha = int(input('Escolha um número de 0 a 5: '))

if escolha == numero:
    print('Você acertou o número secreto')
else:
    print('Você errou o número secreto')

#Solução Guanabara
# from random import randint
# computador = randint(0, 5)




