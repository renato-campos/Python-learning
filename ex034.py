# Curso em Vídeo - Python - Mundo 1
# Data: 07/06/2021
# Exercício 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario_novo = 0
salario_anterior = float(input('Digite o salário do funcionário: R$ '))

if salario_anterior <= 1250:
    salario_novo = salario_anterior * 1.15
else:
    salario_novo = salario_anterior * 1.10

print('O salário anterior de R$ {:.2f} com aulmento passará a R$ {:.2f}'.format(salario_anterior, salario_novo))
