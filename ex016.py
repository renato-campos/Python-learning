# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.
from math import trunc
num = float(input('Digite um número real qualquer: '))

inteira = int(num)
inteira2 = num // 1
inteira3 = trunc(num)
decimal = num - inteira
decimal2 = num % 1

print('A parte inteira é {} e a decimal é {}'.format(inteira, decimal))
print('A parte inteira é {} e a decimal é {}'.format(inteira2, decimal2))
print('A parte inteira é {} e a decimal é {}'.format(inteira3, decimal2))
