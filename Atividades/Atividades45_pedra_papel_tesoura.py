# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random

opcoes_pc = ['pedra', 'papel', 'tesoura']
jogador = int(input('''Escolha sua opção e digite:
 [ 1 ] para PEDRA
 [ 2 ] para PAPEL
 [ 3 ] para TESOURA
 Digite aqui: '''))
computador = random.choice(opcoes_pc)

if jogador == 1 and computador == 'pedra':
    print(f'O computador escolheu {computador} e a rodade empatou')
elif jogador == 1 and computador == 'papel':
    print(f'O computador escolheu {computador} e o jogador perdeu')
elif jogador == 1 and computador == 'tesoura':
    print(f'O computador escolheu {computador} e o jogador venceu')
elif jogador == 2 and computador == 'pedra':
    print(f'O computador escolheu {computador} e o jogador venceu')
elif jogador == 2 and computador == 'papel':
    print(f'O computador escolheu {computador} e a rodada empatou')
elif jogador == 2 and computador == 'tesoura':
    print(f'O computador escolheu {computador} e o jogador perdeu')
elif jogador == 3 and computador == 'pedra':
    print(f'O computador escolheu {computador} e o jogador perdeu')
elif jogador == 3 and computador == 'papel':
    print(f'O computador escolheu {computador} e o jogador venceu')
elif jogador == 3 and computador == 'tesoura':
    print(f'O computador escolheu {computador} a rodade empatou')