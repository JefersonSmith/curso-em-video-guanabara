#ATIVIDADE 17 CURSO EM VIDEO

#Exercício Python 017: Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# catete_oposto = float(input("Digite um numero: "))
# cateto_adjacente = float(input("Digite um numero: "))
#
# hipotenusa = (catete_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
#
# print(f'A hipotenusa é {hipotenusa:.2f}')


import math

catete_oposto = float(input("Digite um numero: "))
cateto_adjacente = float(input("Digite um numero: "))

hipotenusa = math.hypot(catete_oposto, cateto_adjacente)

print(f'A hipotenusa é {hipotenusa:.2f}')