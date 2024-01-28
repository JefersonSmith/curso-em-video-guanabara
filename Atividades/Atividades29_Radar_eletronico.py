# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
#

velocidade = int(input('Qual a velocidade do carro?: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    multa = float(multa)
    print (f'Você foi multado e irá pagar R$ {multa:.2f} de multa')
else:
    print('Você esta dentro do limite de velocidade permitido')