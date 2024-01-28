#ATIVIDADE 15 CURSO EM VIDEO

#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos km você andou com o carro?: "))
dias = int(input("Quandos dias você ficou com o carro?"))

preco = (dias * 60) + (km * 0.15)

print(f"Você ficou {dias} com o carro e rodou {km} Kms, deverá pagar R${preco:.2f}")

