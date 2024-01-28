# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

maiores = 0
homens = 0
mulheres = 0

while True:
    idade = int(input('Qual a sua idade?: '))
    sexo = str(input('Qual o seu sexo? [F/M]: ')).upper()
    if idade > 18:
        maiores += 1
    if sexo == 'F' and idade > 20:
        mulheres += 1
    if sexo == 'M':
        homens += 1
    pergunta = input('Quer continuar? [S/N]: ').upper()
    if pergunta == 'N':
        break
print(f'Existem {maiores} pessoas com mais de 18 anos')
print(f'Existem {homens} homens')
print(f'E {mulheres} mulheres com mais de 20 anos')