# Exercício Python 079: Crie um programa onde o usuário possa digitar
# vários valores numéricos e cadastre-os em uma lista. Caso o número
# já exista lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.

numeros = []
while True:
    teste = int(input('Digite um número: '))
    if teste not in numeros:
        numeros.append(teste)
    else:
        print('Esse valor já foi adicionado')
    pergunta = (input('Quer continuar[S/N]: '))
    if pergunta in 'Nn':
        break
print(sorted(numeros))