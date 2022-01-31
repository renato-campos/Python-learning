# -*- coding: utf-8 -*-
"""
Exercício 4: Construir código em Python que possa medir o valor da temperatura
ambiente e considerar o clima como “Agradável” se a temperatura estiver acima dos
16ºC e até 30ºC ; “Quente” se estiver acima dos 30ºC e considerar “Frio” para
temperaturas até 16ºC.
Created on Fri Sep 03 12:00:00 2021
@author: Renato
"""
# Entrada da temperatura em ºC - Celsius
celsius = float(input('Digite a temperatura em ºC: '))
# Determinação da sensação de conforto
if celsius > 30:
    clima = 'Quente'
else:
    if celsius > 16:
        clima = 'Agradável'
    else:
        clima = 'Frio'
# Exibição dos resultados
print(f'Temperatura:\t{celsius:3.1f}ºC')
print(f'Clima:\t\t\t{clima}')
