#ATIVIDADE 20 CURSO EM VIDEO

# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#import random
from random import shuffle
aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input("Quarto Aluno: "))
alunos = [aluno1, aluno2, aluno3, aluno4]
# random.shuffle(alunos)
shuffle(alunos)

print(f'A ordem da apresentação será: {alunos}')