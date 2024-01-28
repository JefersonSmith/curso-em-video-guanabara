# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Digite aqui a distancia em Km: '))

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print(f'A distância da viagem é de {distancia} Km e você irá pagar R$ {passagem:.2f}')