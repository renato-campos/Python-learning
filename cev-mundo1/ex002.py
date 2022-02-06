# Curso em Vídeo - Python - Mundo 1
# Data: 30/05/2021 rev 02/02/2022
# Exercício 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas para ela:
# Ex:
# Qual é o seu nome? João da Silva
# Olá João da Silva, é um prazer te conhecer!

nome = input('Qual o seu nome? ')
print('Olá {}, é um prazer te conhecer!'.format(nome))      # saída formatada — antiga

print(f'Olá {nome}, é um prazer te conhecer!')              # ideal

print('Olá ' + nome + ', é um prazer te conhecer!')         # trabalhosa

print('Olá', nome, '\b, é um prazer te conhecer!')          # trabalhosa

print('Olá %s, é um prazer te conhecer!' % nome)            # antiga, acho que é herança do Python2
