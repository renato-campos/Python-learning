# -*- coding: utf-8 -*-
"""
Trabalho 1 de Algoritmo - Exercício 2 - 
Escrever código Python para ler através do console as variáveis: 
    “funcionário”, o nome do funcionário de uma empresa; 
    “idade”, a idade do funcionário; 
    “endereço”, o endereço do funcionário; 
    a variável “função”, o cargo do funcionário e 
    a variável “salário”, o valor do seu salário. 
Utilizar o comando print para mostrar os resultados no console. 
Reajustar o salário lido em 20% e mostrar o seu valor atualizado no console.

Created on Fri Aug 27 11:49:09 2021

@author: Renato
"""
# Entrada dos valores das variáveis
nome = input('Digite o nome do funcionário: ')
idade = int(input('Digite a idade: '))
endereço = input('Digite o endereço: ')
função = input('Digite o cargo: ')
salário = float(input('Digite o salário: R$ '))
# Exibição dos Resultados
print('\nInformações do Funcionário:')
print('-' * 27)
print('Nome:\t\t\t', nome)
print('Idade:\t\t\t', idade)
print('Endereço:\t\t', endereço)
print('Cargo:\t\t\t', função)
print(f'Salário Antigo:\t R$ {salário:7.2f}')
print(f'Salário Atual:\t R$ {salário * 1.2:7.2f}')
