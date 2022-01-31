# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite a medida em metros a ser convertida: '))

print('A medida de {:.2f}m equivale a:')
print('{:>8.1f}km'.format(medida / 1000))
print('{:>8.1f}hm'.format(medida / 100))
print('{:>8.1f}dam'.format(medida / 10))
print('{:>8.1f}dm'.format(medida * 10))
print('{:>8.1f}cm'.format(medida * 100))
print('{:>8.1f}mm'.format(medida * 1000))
