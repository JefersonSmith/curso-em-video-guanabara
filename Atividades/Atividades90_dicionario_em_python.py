# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela.

nota = {}
nota['nome'] = str(input('Qual seu nome: '))
nota['media'] = int(input('Qual sua media: '))
if nota['media'] >= 6:
    nota['situacao'] = 'Aprovado'
elif nota['media'] < 6:
    nota['situacao'] = 'Reprovado'


print(f'O nome é {nota["nome"]}')
print(f'A media é {nota["media"]}')
print(f'A situação é {nota["situacao"]}')

