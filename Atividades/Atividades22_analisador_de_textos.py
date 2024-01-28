# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# – O nome com todas as letras maiúsculas e minúsculas.
#
# – Quantas letras ao todo (sem considerar espaços).
#
# – Quantas letras tem o primeiro nome.

nome = input('Qual seu nome completo? ')
nome_s = nome.split()
nome_r = nome.strip()
total_nome = len(nome_r) - nome.count(' ')

print('Seu nome em letras maíusculas é ', nome.upper())
print('Seu nome em letras minúsculas é ', nome.lower())
print(f'Seu nome tem ao todo {total_nome} letras')
print(f'Seu primeiro nome é {nome_s[0]} e ele tem {len(nome_s[0])} letras')
