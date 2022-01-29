# -*- coding: utf-8 -*-
"""
Exercício 04: Simulado de Diagnóstico médico com operadores lógicos e relacionais.
Escrever código Python para a proposição:pessoa está com a
temperatura maior que 37ºC e dor de cabeça ou coriza -> gripe = verdadeiro
Atribuir no código Python valores para a temperatura (dado do tipo numérico
inteiro) e para dor de cabeça e coriza (dado do tipo lógico) e simular se o
diagnóstico é de gripe. Imprimir algumas combinações da proposição no console.
Inserir os dados pelo console.

Created on Fri Aug 20 11:00:40 2021

@author: Renato
"""

# Entrada de dados
print('*-' * 10,'Diagnóstico Online', '*-' * 10)
temp = float(input('Informe sua temperatura em ºC: '))
dor = input('Você está com dor de cabeça?'.lower())
coriza = input('Você tem coriza?'.lower())

# decisão
gripe = temp > 37 and dor == "sim" or coriza == 'sim'

# exibindo resultado
print('Resultado para Gripe: ', gripe)
