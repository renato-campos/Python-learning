# -*- coding: utf-8 -*-
"""
Exercício 3.3 Cálculo da média
Inserir na aplicação as matérias Educação Física e Geografia criar
uma variável nome que irá receber o primeiro nome do aluno criar uma
variável sobrenome para receber o sobrenome do aluno Inserir os valores
das notas relativas às cinco matérias, assim como o nome completo do
aluno, via console Mostrar no console o nome completo do aluno (nome
e sobrenome concatenados), os valores das notas e a média recalculada.

Created on Thu Aug 26 20:56:53 2021

@author: Renato
"""
nome = input('Digite o nome do aluno: ')
sobrenome = input('Digite o sobrenome do aluno: ')
media = 0.0
portugues = float(input('Digite a nota de Português: '))
matematica = float(input('Digite a nota de Matemática: '))
historia = float(input('Digite a nota de História: '))
educfisica = float(input('Digite a nota de Educação Física: '))
geografia = float(input('Digite a nota de Geografia: '))
media = (portugues + matematica + historia + educfisica + geografia)/5
print()
print('*' * 10, 'NOTAS', '*' * 10)
print('Aluno: ', nome, sobrenome)
print('Português:\t\t', portugues)
print('Matemática:\t\t', matematica)
print('História:\t\t', historia)
print('Educação Física:', educfisica)
print('Geogragia:\t\t', geografia)
print('-' * 27)
print('Média:\t\t\t', media)
