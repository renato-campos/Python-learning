# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$ '))

salario *= 1.15

print('O salário do funcionário com aumento passará a R${:.2f}'.format(salario))
