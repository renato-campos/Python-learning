# Curso em Vídeo - Python - Mundo 1
# Data: 07/06/2021
# Exercício 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from random import randint

n1 = randint(-10, 10)
n2 = randint(-10, 10)
n3 = randint(-10, 10)

maior = menor = n1

if n2 > maior:
    maior = n2
else:
    menor = n2
if n3 > maior:
    maior = n3
else:
    if n3 < menor:
        menor = n3

print('Entre os números {}, {} e {}, o maior é {} e o menor {}'.format(n1, n2, n3, maior, menor))

# outro opção

if n1 > n2:
    maior, menor = n1, n2
else:
    maior, menor = n2, n1
if n3 > maior:
    maior = n3
else:
    if n3 < menor:
        menor = n3

print('Entre os números {}, {} e {}, o maior é {} e o menor {}'.format(n1, n2, n3, maior, menor))
