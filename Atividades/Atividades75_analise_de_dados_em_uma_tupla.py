# Exercício Python 075: Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

v1 = int(input('Digite um número: '))
v2 = int(input('Digite um número: '))
v3 = int(input('Digite um número: '))
v4 = int(input('Digite um número: '))
valores = (v1, v2, v3, v4)



if 9 in valores:
    nove = valores.count(9)
    print(f'O número nove apareceu {nove} veze(s)')
if 3 in valores:
    tres = valores.index(3)
    print(f'O número 3 apareceu na posição {tres + 1}')
print('Os números pares são: ', end='')
for i in valores:
    if i % 2 == 0:
        print(f'{i} ', end='')