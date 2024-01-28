# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numero = int(input('Digite um número: '))
cont = 0
soma = 0
maior = 0
menor = 999999999
continuar = 'S'


while continuar in 'Ss':
    cont += 1
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar in 'Ss':
        numero = int(input('Digite um número: '))

media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
