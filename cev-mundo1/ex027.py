# Curso em Vídeo - Python - Mundo 1
# Data: 06/06/2021
# Exercício 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.)

nome = str(input('Digite seu nome completo: ')).strip().title().split()

print('O primeiro nome é {}'.format(nome[0]))
print('O último nome é {}'.format(nome[-1]))
