# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ')
nome_lista = nome.split()
print(f'Seu primeiro e último nome é {nome_lista[0]} {nome_lista[-1]}')