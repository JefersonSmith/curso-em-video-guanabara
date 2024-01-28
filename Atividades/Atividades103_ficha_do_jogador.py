# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='', gols=0):
    nome = str(input('Nome do jogador: '))
    gols = str(input('Número de gols: '))
    if nome == '':
        nome = 'Não informado'
    if gols == '':
        gols = 0

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')



ficha()