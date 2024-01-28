#ATIVIDADE 11 CURSO EM VIDEO

#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Qual a largura de sua parede?: "))
altura = float(input("Qual a altura de sua parede?: "))

area = largura * altura
tinta = area / 2

print(f'Sua parede tem uma área de {area:.2f} m2 e você irá precisar de {tinta:.2f} litros de tinta')