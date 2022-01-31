# -*- coding: utf-8 -*-
"""
Trabalho 1 - Exercício 4: Um desenvolvedor de software para uma estação meteorológica
tem que fazer a leitura das seguintes variáveis, para o dia corrente e dar previsões
para o dia seguinte, conforme as condições:
- variáveis:
→ Temperatura;
→ Umidade Relativa do Ar;
- condições:
Se (Temperatura >= 28ºC e Umidade Relativa do Ar >= 50%) Previsão: “irá chover amanhã”;
Senão Previsão: “amanhã o dia será sem chuvas”;
- Escrever código em Python para ler as variáveis, mostrar os seus valores no console;
- Mostrar a previsão do tempo para o dia seguinte, simulando algumas possibilidades.
Created on Fri Aug 27 11:53:04 2021

@author: Renato
"""
# Leitura das variáveis
temperatura = float(input('Digite a temperatura ºC: '))
umidade = int(input('Digite a % da Umidade Relativa do Ar: '))
# Determinação da previsão do tempo
if temperatura >= 28 and umidade >= 50:
    previsão = 'irá chover amanhã.'
else:
    previsão = 'amanhã o dia será sem chuvas.'
# Exibição dos resultados
print()
print('*' * 10, 'Previsão do tempo', '*' * 10)
print(f'''Dadas as leituras:
Temperatura {temperatura:.1f}ºC
Umidade Relativa do Ar {umidade}%\n
A previsão do tempo é de que
{previsão}''')
