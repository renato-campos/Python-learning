# Curso em Vídeo - Python - Mundo 1
# Data: 06/06/2021
# Exercício 035:  Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print('Digite a medida de 3 segmentos de retas:')
a = float(input('Primeiro: '))
b = float(input('Segundo: '))
c = float(input('Terceiro: '))

if a < b + c and b < a + c and c < a + b:
    print('Os 3 segmentos PODEM formar 1 triângulo.')
else:
    print('Esses 3 segmentos NÃO PODEM formar 1 triângulo.')
