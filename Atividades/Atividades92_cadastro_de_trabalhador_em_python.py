# Exercício Python 092: Crie um programa que leia nome,
# ano de nascimento e carteira de trabalho e cadastre-o
# (com idade) em um dicionário. Se por acaso a CTPS for
#     diferente de ZERO, o dicionário receberá também o
#     ano de contratação e o salário. Calcule e acrescente,
#     além da idade, com quantos anos a pessoa vai se aposentar.

# dados = {}
#
# while True:
#     dados['nome'] = str(input('Nome: '))
#     dados['idade'] = int(input('Ano de Nascimento: '))
#     dados['ctps'] = int(input('Carteira de Trabalho (0 não tem):  '))
#     if dados['ctps'] == 0:
#         break
#     dados['ano'] = int(input('Ano de Contratação:  '))
#     dados['salario'] = int(input('Salário:  '))
#     break
# print(f'o nome tem valor {dados["nome"]}')
# print(f'idade tem valor {2023 - dados["idade"]}')
# print(f'ctps tem valor {dados["ctps"]}')
# if dados['ctps'] != 0:
#     print(f'contratação tem valor {dados["ano"]}')
#     print(f'Salário tem valor {dados["salario"]}')
#     print(f'Aposentadoria tem o valor {(dados["ano"] + 35) - dados["idade"]}')

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Anod e Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print(('-=' * 30))
for k, v in dados.items():
    print(f'{k} tem o valor {v}')