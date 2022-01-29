# Curso em Vídeo - Python - Mundo 1
# Data: 06/06/2021
# Exercício 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime

ano = int(input('Digite o ano: (0 para atual)'))                # seleção da data atual importando módulo
if ano == 0:
    ano = datetime.date.today().year

if ano <= 1582:                                                 # algoritmo com if's aninhados
    print('O Calendário Gregoriano teve início em 1582.')
else:
    if ano % 4:
        print('Não é Ano Bissexto.')
    else:
        if ano % 100:
            print('Ano Bissexto')
        else:
            if ano % 400:
                print('Não é Ano Bissexto.')
            else:
                print('Ano Bissexto.')

if ano <= 1582:
    print('O Calendário Gregoriano teve início apenas em 1582.')
else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:           # condicional com operaçóes lógicas
        print('Ano Bissexto.')                                      # melhor que o anterior
    else:
        print('Não é ano Bissexto.')
