# -*- coding: utf-8 -*-
"""
Exercício 3.3: escrever código Python para verificar os resultados das expressões:
a) True or False and not True (justificar o resultadp)
b) salário > 1000 and idade > 18  atribuir valores para salário e idade.
c) Utilizar a expressão A > B and C or D para completar os resultados da
tabela 
A (1, 10, 5)
B (2, 3, 1)
C (V, F, V)
D (F, F, V)
(escrever o código Python)
        
Created on Fri Aug 13 12:24:57 2021

@author: Renato
"""
# parte A
print('resultado de "not True" = ', not True)
print('resultado de "False and not True" = ', False and not True)
print('resultado de "True or False and not True" = ', True or False and not True)
print()
# parte B
salario = 1300
idade = 13
print('Salário > 1000 e Idade > 18 ', salario > 1000 and idade > 18)
print()
# parte C
print('1 > 2 and True or False = ', 1 > 2 and True or False)
print('10 > 3 and False or False = ', 10 > 3 and False or False)
print('5 > 1 and True or True = ', 5 > 1 and True or True)
