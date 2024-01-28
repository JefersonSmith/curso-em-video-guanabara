# Exercício Python 094: Crie um programa que leia nome,
# sexo e idade de várias pessoas, guardando os dados de
# cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = {}
user = []
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo [M/F]: '))
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    continuar = str(input('Quer continuar? [S/N]: '))
    user.append(pessoas.copy())
    if continuar in 'Nn':
        break

print(user)
print(f'Foram cadastradas {len(user)} pessoas')
media = soma / len(user)
print(f' A media deidade das pessoas cadastradas é {media}')
print(f'As mulheres cadastradas foram: ')
for p in user:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ')
print('Lista das pessoas que estão acima de média: ')
for p in user:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('Encerrado')