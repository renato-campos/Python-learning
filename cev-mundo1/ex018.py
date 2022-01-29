# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 018: Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input('Digite a medida do ângulo em graus: '))

seno = round(math.sin(math.radians(angulo)), 2)
cosseno = round(math.cos(math.radians(angulo)), 2)
tangente = round(seno / cosseno, 2)
tangente2 = round(math.tan(math.radians(angulo)), 2)

print('O seno vale {}, o cosseno {} e a tangente {} ou {}'.format(seno, cosseno, tangente, tangente2))
