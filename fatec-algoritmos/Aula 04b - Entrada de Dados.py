# -*- coding: utf-8 -*-
"""
Aula 04b: Entrada de Dados

Created on Fri Aug 20 10:23:32 2021

@author: Renato
"""

# entrada de dados pelo console
idade = int(input('idade = '))
print(idade)
nome = input('nome: ')
print(nome)
salario = float(input('digite salário: R$ '))
print('R$', salario)

print('verificando idade', idade < 55)
print('verificando nome', nome == "Renato")
print('verificando salário', salario >= 1698.88)
