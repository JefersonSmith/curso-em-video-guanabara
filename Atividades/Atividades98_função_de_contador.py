# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
# três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

# def contador(inicio, fim, passo):
#     for i in range(inicio, fim, passo):
#         print(i,end=' ')
#         sleep(0.3)
#
# contador(1, 11, 1)
# print()
# contador(10, -1, -2)
# print()
# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# contador(i, f, p)

def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Jeferson Smith!
    """
    if p < 0:
        p *= -1
    if p == 0:
        p == 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont -= p
        print('Fim!')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)