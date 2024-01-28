# Exercício Python 088: Faça um programa que ajude um jogador da
# MEGA SENA a criar palpites.O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para
# cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogos = int(input('Quantos jogos você quer fazer?: '))
mega = []
for jogo in range (1, jogos + 1):
    for numero in range(0,6):
        mega.append(randint(1, 60))
    mega.sort()
    print(f'o {jogo}º jogo é {mega}')
    sleep(1)
    mega.clear()
print('Boa Sorte!')