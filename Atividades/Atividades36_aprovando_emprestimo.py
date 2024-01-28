# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

valor = int(input('Qual o valor da casa?: '))
salario = int(input('Qual o seu salário?: '))
prazo = int(input('Em quantos anos você irá pagar?: '))
total_mensalidades = prazo * 12

if (valor / total_mensalidades) < salario * 0.30:
    print(f'O valor da casa é {valor}, dividido em {total_mensalidades} parcelas'
          f' e o valor de cada parcela é R$ {valor / total_mensalidades:.2f}. Você pode pagar por isso')
else:
    print('Você não pode pagar pelo empréstimo')




