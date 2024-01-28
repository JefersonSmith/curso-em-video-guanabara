#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Digite aqui o seu nome: ')

lista_nome = nome.upper().split()

print('SILVA' in lista_nome)