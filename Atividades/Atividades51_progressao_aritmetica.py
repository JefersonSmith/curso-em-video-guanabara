# Exercício Python 51: Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for i in range (0, 10):
    termo = termo + razao
    print(termo - razao)
print('ACABOU')