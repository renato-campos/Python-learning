# -*- coding: utf-8 -*-
"""
Trabalho 1 de Algoritmo - Exercício 1 - Teste de Variáveis
Escrever código Python para testar os valores das variáveis A à F na tabela
e mostrar os resultados no console, para a expressão:
Inserir os valores pelo console.  
A ≤ B or not C or D > E and F
A       B    	C	    D 	    E 	    F 	     resultado 
2.4 	2.5 	True 	0.6 	0.9 	True 	 
-3.6 	-3.59 	False 	-0.08 	-0.09 	True 	 
1.1 	1.1 	True 	3.0 	3.0 	False 	 
7.8 	6.4 	False 	5.0 	-5.0 	True 	 
A ≤ B or not C or D > E and F
Created on Fri Aug 27 10:25:54 2021
@author: Renato
"""

# Entrada das variáveis
print('Digite os Valores das Variáveis conforme a Tabela:')
A = float(input('Digite o valor da variável A:\t'))
B = float(input('Digite o valor da variável B:\t'))
C = bool(input('Digite o valor da variável C:\t'))
D = float(input('Digite o valor da variável D:\t'))
E = float(input('Digite o valor da variável E:\t'))
F = bool(input('Digite o valor da variável F:\t'))
# Cálculo da expressão
resultado = A <= B or not C or D > E and F
# Exibição do Resultado
print(f'''Sendo:
      A = {A}   B = {B}   C = {C}
      D = {D}   E = {E}   F = {F}
      Resultado = {resultado}''')
