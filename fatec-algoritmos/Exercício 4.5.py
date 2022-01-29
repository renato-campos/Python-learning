# -*- coding: utf-8 -*-
"""
Exercício 5: Construir código em Python que receba a estação do ano e retorne os
respectivos meses que a mesma compreende.
Created on Fri Sep 03 12:00:00 2021
@author: Renato
"""
season = input('Digite a estação do ano: ').upper()
if season == 'VERÃO':
    months = 'Dezembro, Janeiro, Fevereiro e Março'
else:
    if season == 'OUTONO':
        months = 'Março, Abril, Maio e Junho'
    else:
        if season == 'INVERNO':
            months = 'Junho, Julho, Agosto e Setembro'
        else:
            if season == 'PRIMAVERA':
                months = 'Setembro, Outubro, Novembro e Dezembro'
            else:
                months = 'Estação informada incorretamente'
print('\nEstação:', season)
print('Meses:', months)
