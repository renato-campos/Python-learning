# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 003: Crie um programa que leia dois números e mostre a soma entre eles.

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

num1, num2 = float(num1), float(num2)
soma = num1 + num2
print('A soma entre {} e {} agora sim resulta {}'.format(num1, num2, soma))

num3 = float(input('Digite um número: '))
num4 = float(input('Digite outro número: '))
soma = num3 + num4
print('A soma entre {} e {} resulta {}'.format(num3, num4, soma))
