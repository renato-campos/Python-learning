# -*- coding: utf-8 -*-
"""
Aula 03a: Referência do objeto - Tipagem dinâmica

Created on Fri Aug 13 10:28:09 2021

@author: Renato
"""

# Uma referência de objeto (variável) assume o valor de um tipo de dado
# através do operador '='
cor = 'azul'    # cor  tipo string
numero = 6      # número tipo inteiro
print('a cor é: ', cor)
print('o número é: ', numero)

# o valor do objeto (variável) pode ser mutável, independentemente do tipo
# Python utiliza tipagem dinâmica

cor = numero
print('o número é: ', cor)

# redefinição dos valores
cor = 'laranja'
numero = 19

# imprimindo os tipos de dados das variáveis - '\n' muda de linha
print('a cor é: ', cor, '\ntipo de dado: ', type(cor))
print('o número é: ', numero, '\ntipo de dado: ', type(numero))
