# Exercício Python 61: Refaça o DESAFIO 51,
# lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Exercício Python 62: Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print(termo)
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print(f'Progressão finalizada com {total} termos mostrador')