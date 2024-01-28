# Exercício Python 076: Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = ('Lápis', 1.75,
         'Borracha', 2.0,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for posicao in range(0, len(tupla)):
    if posicao % 2 == 0:
        print(f'{tupla[posicao]:.<30}', end='')
    else:
        print(f'R${tupla[posicao]:>7.2f}')

