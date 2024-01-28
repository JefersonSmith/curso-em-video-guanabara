# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

from random import randint
#
# n1= randint(0, 100)
# n2= randint(0, 100)
# n3= randint(0, 100)
# n4= randint(0, 100)
# n5= randint(0, 100)
#
# tupla = (n1, n2, n3, n4, n5)
# tupla_organizada = sorted(tupla)
# print(tupla)
# print(f'O maior número da tupla foi {tupla_organizada[-1]} e o menor foi {tupla_organizada[0]}')

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')