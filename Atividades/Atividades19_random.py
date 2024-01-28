#ATIVIDADE 19 CURSO EM VIDEO

#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input("Quarto Aluno: "))
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(alunos)

print(f'O aluno escolhido foi: {escolhido}')