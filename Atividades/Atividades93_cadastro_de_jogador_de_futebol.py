# Exercício Python 093: Crie um programa que gerencie o aproveitamento
# de um jogador de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

jogador = {}
total = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantoas partidas {jogador["nome"]} jogou?: '))
for partida in range(0, partidas):
    total.append(int(input(f'Quantos gols na partida {partida}?: ')))
jogador['gols'] = total[:]
jogador['total'] = sum(total)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' Na partida {i} , fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')