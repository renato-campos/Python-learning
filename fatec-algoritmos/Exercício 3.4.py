# -*- coding: utf-8 -*-
"""
Exercício 3.4: Com base no exercício anterior verificar a média ;
se a mesma for maior ou igual a 5.0, mostrar no console 
a mensagem →“aluno aprovado”; se a média for menor que 5.0, 
mostrar no console a mensagem →“aluno reprovado”;

Created on Thu Aug 26 21:15:42 2021

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
    result = '\033[1;32mAPROVADO\033[m'
if media < 5.0:
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
