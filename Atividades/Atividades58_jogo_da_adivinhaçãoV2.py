# Exercício Python 58: Melhore o jogo do DESAFIO 28
# onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
escolha = 11
palpite = 0

while escolha != computador:
    escolha = int(input('Escolha um número de 0 a 10: '))
    if escolha != computador:
       if escolha < computador:
           print('Mais... tente novamente')
       else:
           if escolha > computador:
               print('Menos... tenve novamente!')
    palpite += 1
print(f'Você acertou o número escolhido e precisou de {palpite} tentativas')

#Guanabara
# computador = randint (0, 10)
# print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
# print('Será que você consegue adivinhar qual foi? ')
# acertou = False
# palpites = 0
# while not acertou:
#     jogador = int(input('Qual é seu palpite?: '))
#     palpites += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print('Mais... tente mais uma vez')
#         elif jogador > computador:
#             print('Menos... tente mais uma vez')
# print(f'Acertou! Precisou de {palpites} tentativas')
