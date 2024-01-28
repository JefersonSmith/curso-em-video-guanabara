# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

sistema = True

while sistema is True:
    a = int(input('Escolha um número: '))
    b = int(input('Escolha outro número: '))
    pergunta = str(input('''Qual é a sua opção?:
    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Digite aqui a opção escolhida: '''))
    if pergunta == "1":
        print('A soma dos números escolhidos é', a +  b)
    elif pergunta == "2":
        print('A multiplicação dos números escolihos é', a * b)
    elif pergunta == "3":
        if a > b:
            print(f'O maior número é {a}')
        else:
            print(f'O maior número é {b}')
    elif pergunta not in "12345":
        print('Você digitou uma opção que não existe')
    elif pergunta == "5":
        sistema = False
print('Você encerrou o programa')



