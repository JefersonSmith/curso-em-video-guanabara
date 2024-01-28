#ATIVIDADE 10 CURSO EM VIDEO

#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input("Quantos reais você tem na carteira?: "))

cotacao = 5.80

dolar = dinheiro / cotacao

print(f'Você pode comprar US$ {dolar:.2f}, com o dinheiro que você tem')