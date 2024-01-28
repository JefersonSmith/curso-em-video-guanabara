# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número
# pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')



while True:
    escolha = int(input('Digite um número de 0 a 20: '))
    if escolha > 20:
        print('Você deve digitar um número entre 0 e 20')
    else:
        print(f'O número que você escolheu por extenso é: {numeros[escolha - 1]}')


