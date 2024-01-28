# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time do Fortaleza.

tabela = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional', 'Fluminense', 'Cruzeiro', 'Gremio',
          'Sao Paulo', 'Vasco', 'Atletico', 'Santos', 'Bragantino', 'Flamengo', 'Athletico', 'Bahia', 'Goias',
          'Corinthians', 'Cuiaba', 'Coritiba', 'America')

print('Os cinco primeiros colocados são:', tabela[0:5])
print('Os quatro últimos colocados são:', tabela[16:])
print('Tabela em ordem alfabética: ', sorted(tabela))
fortaleza = tabela.index('Fortaleza')
posicao_fortaleza = fortaleza + 1
print(f'O time do Fortaleza está em {posicao_fortaleza}° colocado')


