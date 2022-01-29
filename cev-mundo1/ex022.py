# Curso em Vídeo - Python - Mundo 1
# Data: 04/06/2021
# Exercício 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras no total (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
nome1 = nome.split()
print(len(nome1[0]))
# outro modo
print(nome.find(' '))
