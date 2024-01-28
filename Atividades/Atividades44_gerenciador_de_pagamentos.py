# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

preco = float(input('Qual o valor do produto?: '))
condicao = (int(input('''Escolha sua opção de pagamento:
[ 1 ] à vista no dinheiro ou pix
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
Digite aqui: ''')))

if condicao == 1:
    preco = preco - preco * 0.10
    print(f'Você irá pagar pelo produto R$ {preco:.2f}')
elif condicao == 2:
    preco = preco - preco * 0.05
    print(f'Você irá pagar pelo produto R$ {preco:.2f}')
elif condicao == 3:
    print(f'Você irá pagar pelo produto R$ {preco:.2f}')
elif condicao == 4:
    preco = preco + preco * 0.20
    print(f'Você irá pagar pelo produto R$ {preco:.2f}')
else:
    print("Você escolheu uma opçãoe errada")
