# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições.


# UTILIZANDO PRINT

def voto(ano):
    idade = 2023 - ano
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO.')
    elif idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


pergunta = int(input('Em que ano você nasceu?: '))
voto(pergunta)


# UTILIZANDO RETURN

def voto(ano):
    idade = 2023 - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


pergunta = int(input('Em que ano você nasceu?: '))
print(voto(pergunta))
