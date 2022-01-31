# -*- coding: utf-8 -*-
"""
Aula 02 - Teoria - Variáveis, Tipos e função print( )

Created on Fri Aug  6 23:12:59 2021

@author: Renato

"""
# Comentários em uma linha podem ser precedidos por 'jogo da velha #'

'''Comentários em mais de uma linha devem
estar entre 3 aspas, simples ou duplas
'''

# Atribuições de valores a variáveis do tipo inteiro - int
a = 12
b = -8

# Atribuições de valores a variáveis do tipo string - str
c = 'Ciência de Dados'
d = "@*$?"
e = ''
f = '88'

# Comando de impressão no console - print
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
print('e = ', e)
print('f = ', f)

# Conversão de string para inteiro
h = int(f)
g = b + h
print('g = (-8) + 88 = ', g)

# Conversão de inteiro para string
str(a)          # pq não funcionou? teria que reatribuir?
print(a)
print(type(a))
a = str(a)      # aqui funcionou!
print(a)
print(type(a))

a = c
print('a: string = ', a)
