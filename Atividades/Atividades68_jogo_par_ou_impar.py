# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

total = 0

while True:
    computador = randint(0, 11)
    player = int(input('Digite um numero: '))
    if (computador + player) % 2 == 0:
        print(f'Você escolheu {player} e o computador escolheu {computador}')
        print('Jogador venceu!')
        total += 1
    else:
        print(f'Você escolheu {player} e o computador escolheu {computador}')
        print('Você perdeu!')
        break
print(f'O jogador venceu {total} partidas seguidas')