# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = float(input('Digite um número: '))

print('''O número {} tem como
seu dobro o {},
seu triplo o {} e
como sua raiz quadrada o {}'''.format(num, 2 * num, 3 * num, num ** (1/2)))

# Cálculo de raiz quadrada:

rz1 = num ** 0.5
rz2 = num ** (1 / 2)
rz3 = pow(num, 1 / 2)

from math import sqrt

rz4 = sqrt(num)

print('Raizes quadradas calculadas de formas diferentes', rz1, rz2, rz3, rz4)
print(rz1 == rz2, rz1 == rz3, rz1 == rz4)
print(rz3 == rz2, rz2 == rz4)
print(rz3 == rz4)
