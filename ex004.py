# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 004: Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

var = input('Digite algo: ')

print('Seu tipo primitivo é', type(var))
print('Só tem espaços? ', var.isspace())
print('É alfanumérico? ', var.isalnum())
print('É alfabético? ', var.isalpha())
print('É caracter ASCII? ', var.isascii())
print('É um dígito? ', var.isdigit())
print('É número decimal?', var.isdecimal())
print('É usado como identificador?', var.isidentifier())
print('É numérico? ', var.isnumeric())
print('É imprimível? ', var.isprintable())
print('Está em letras minúsculas', var.islower())
print('Está em letras maiúsculas', var.isupper())
print('Está capitalizada? ', var.istitle())

print('teste'.upper())
print('teste'.title())
print('TESTE'.lower())
