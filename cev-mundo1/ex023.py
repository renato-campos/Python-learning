# Curso em Vídeo - Python - Mundo 1
# Data: 05/06/2021
# Exercício 023: Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número entre 0 e 9999: '))

print(numero // 1000)
num = numero % 1000
print(num // 100)
num %= 100
print(num // 10)
print(num % 10)

# OUTRO MODO
print('*' * 40)
print(numero // 1 % 10)
print(numero // 10 % 10)
print(numero // 100 % 10)
print(numero // 1000 % 10)
