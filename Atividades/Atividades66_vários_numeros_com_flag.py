# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre elas (desconsiderando o flag).


cont = soma = 0
while True:
    numero = int(input('Digite um número [999 para encerrar]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero

print(f'Foram digitados {cont} números e a soma total entre eles é {soma}')