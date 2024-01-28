# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

def area(largura, comprimento):
    area_total = largura * comprimento
    print(f'A áre de um terreno {largura} x {comprimento} é de {area_total}m²')


area(largura, comprimento)