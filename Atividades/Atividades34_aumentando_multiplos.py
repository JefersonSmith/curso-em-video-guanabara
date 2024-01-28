# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário?: '))

if salario > 1250:
    salario = salario + salario * 0.1
else:
    salario = salario + salario * 0.15

print(f'O seu salário agora será de R$ {salario}')

