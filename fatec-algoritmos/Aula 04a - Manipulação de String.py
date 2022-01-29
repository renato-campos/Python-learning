# -*- coding: utf-8 -*-
"""
Aula 04a : Manipulação de String

Created on Fri Aug 20 09:40:50 2021

@author: Renato
"""

# dimensão de uma string - len( )
a = 'Maurício'
print('dimensão da string a = ', len(a))
print('dimensão da string com espaço = ', len('a b'))
print('dimensão da string vazia = ', len(''))

# acesso de caracteres de strings
print('primeira letra de Maurício = ', a[0])
c = "a b"
print('valor entre a e b = ', c[1])
d = 'abc'
print('valor entre a e c = ', d[1])

# strings concatenadas
e = ' Conceição Mario'
print('nome do professor', a + e)
print('M' * 5)
print('-*' * 10 + '-')
