# Curso em Vídeo - Python - Mundo 1
# Data: 06/06/2021
# Exercício 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número inteiro: '))

if numero % 2:
    print('O número {} é ímpar.'.format(numero))
else:
    print('O número {} é par.'.format(numero))
