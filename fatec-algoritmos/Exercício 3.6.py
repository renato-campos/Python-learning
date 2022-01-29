# -*- coding: utf-8 -*-
"""
Exercício 6 : Construir aplicação Python para receber pelo console
os seguintes dados de um contribuinte do Imposto de Renda:
- Identificação
- Endereço
- CPF
- Renda Anual
- Imposto Pago
O valor de isenção do imposto é de R$ 44.000,00 anuais. O cálculo do imposto é:
Imposto = Renda Anual * 15% - Imposto Pago
Mostrar também no console os dados do contribuinte e o resultado do imposto,
a pagar ou restituir (simular para que possam ocorrer as duas situações).

Created on Thu Aug 26 21:34:11 2021

@author: Renato
"""

nome = input('Digite o nome completo: ')
endereço = input('Digite o endereço: ')
cpf = input('Digite o CPF: ')
renda = float(input('Digite o valor da Renda Anual: R$ '))
pago = float(input('Digite o valor do Imposto Pago: R$ '))
print('\nInformações do Contribuinte:')
print('Nome:\t\t', nome)
print('Endereço:\t',endereço)
print('CPF:\t\t', cpf)
print(f'Renda Anual:\t\tR$ {renda:10.2f}')
print(f'Imposto Pago:\t\tR$ {pago:10.2f}')
if renda <= 44000:
    imposto = pago
    print(f'Imposto a restituir:\033[1;32mR$ {imposto:10.2f}\033[m')
else:
    imposto = renda * 0.15 - pago
    print(f'Imposto a pagar:\t\033[1;31mR$ {imposto:10.2f}\033[m')
