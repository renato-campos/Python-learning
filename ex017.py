# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 017: Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot, sqrt

co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))

hip = hypot(co, ca)
hip2 = sqrt(co**2 + ca**2)

print('A medida da hipotenusa é {:.2f} e {:.2f}'.format(hip, hip2))
