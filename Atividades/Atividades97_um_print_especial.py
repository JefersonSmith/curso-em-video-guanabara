# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

frase = str(input('Digite uma frase: '))
frase2 = str(input('Digite uma frase: '))
frase3 = str(input('Digite uma frase: '))


def escreva(frase):
    print('~' * len(frase))
    print(frase)
    print('~' * len(frase))


escreva(frase)
escreva(frase2)
escreva(frase3)

