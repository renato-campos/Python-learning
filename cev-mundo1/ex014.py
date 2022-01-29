# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 014: Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em ºC: '))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273

print('Os {:.1f}ºC equivalem a {:.1f}ºF ou {:.1f}K'.format(celsius, fahrenheit, kelvin))
