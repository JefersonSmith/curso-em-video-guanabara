#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite aqui o nome da cidade: ').strip()

print(cidade[:5].upper() == 'SANTO')