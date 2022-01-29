# -*- coding: utf-8 -*-
"""
Exercício 3.5: Com base no exercício anterior verificar a média
e a aprovação do aluno só que usando a estrutura if - else

Created on Thu Aug 26 21:30:08 2021

@author: Renato
"""

nome = input('Digite o nome do aluno: ')
sobrenome = input('Digite o sobrenome do aluno: ')
media = result = 0.0
portugues = float(input('Digite a nota de Português: '))
matematica = float(input('Digite a nota de Matemática: '))
historia = float(input('Digite a nota de História: '))
educfisica = float(input('Digite a nota de Educação Física: '))
geografia = float(input('Digite a nota de Geografia: '))
media = (portugues + matematica + historia + educfisica + geografia)/5
if media >= 5.0:
    cond = 'média >= 5.0'
    result = '\033[1;32mAPROVADO\033[m'
else:
    cond = 'média < 5.0'
    result = '\033[1;31mREPROVADO\033[m'
print()
print('*' * 10, 'NOTAS', '*' * 10)
print('Aluno: ', nome, sobrenome)
print('Português:\t\t', portugues)
print('Matemática:\t\t', matematica)
print('História:\t\t', historia)
print('Educação Física:', educfisica)
print('Geogragia:\t\t', geografia)
print('-' * 27)
print('Média:\t\t\t', media, ' -> ', result)
print('Estado da Condição -> True para', cond)