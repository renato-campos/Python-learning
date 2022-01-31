# -*- coding: utf-8 -*-
"""
Aula 3: Operadores Relacionais e Operadores Lógicos

Created on Fri Aug 13 11:55:50 2021

@author: Renato
"""

# Operadores relacionais
a = 1
b = 2
c = 2
print('a igual b - \t\t\t', a == b)
print('a diferente b - \t\t', a!= b)
print('b maior que b - \t\t', b > a)
print('a menor ou igual a b - ', a<= b)
print('c maior ou igual a b - ', c>= b)

# Exemplo (Menezes, 2019):
nota = 8
media = 7
aprovado = nota >= media
print('resultado da verificação da aprovação = ', aprovado)

# Operadores Lógicos
# not = não
# and = e
# or = ou

V = True
F = False
# Exemplo para operador 'not'
print('complemento de True = ', not V)
print('coplemento de False = ', not F)
# Exemplo de operador 'and'
print('True and True = ', V and V)
print('True and False = ', V and F)
print('False and False = ', F and F)
# Exemplo para operador 'or'
print('True or True = ', V or V)
print('True or False = ', V or F)
print('False or False = ', F or F)
