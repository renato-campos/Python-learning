# -*- coding: utf-8 -*-
"""
Exercício 2: Construir código em Python que possa ler a quantidade de peças de roupas a ser compradas por um cliente
em uma loja de atacado. Se a quantidade de peças de roupa for igual ou superior a 30, o preço por peça é R$ 20,00.
Se comprar de 20 a 30 peças, o preço por peça é de R$ 28,00. Se comprar menos de 20 peças o preço por peça é R$ 35,00.
Usando condicionais aninhadas.
Created on Fri Sep 03 11:04:11 2021
@author: Renato
"""

# Entrada da qunatidade de roupas compradas
quantity = int(input('Quantidade de peças de roupas: '))
# Condicional para definição do preço por peça de roupa
if quantity >= 30:
    unit_price = 20
else:
    if quantity < 20:
        unit_price = 35
    else:
        unit_price = 28
# Cálculo e exibição do resultado
print(f'Quantidade de peças: {quantity:16}')
print(f'Preço por unidade de roupa = R$ {unit_price:8.2f}')
print(f'Valor da compra              R$ {quantity * unit_price:8.2f}')
