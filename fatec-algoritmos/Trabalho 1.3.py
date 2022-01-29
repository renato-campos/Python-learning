# -*- coding: utf-8 -*-
"""
Trabalho 1 de Algoritmo - Exercício 3
Em uma compra de supermercado, foram adquiridos os seguintes itens e quantidades:
- Arroz → 5kg;
- Feijão → 3kg;
- Açúcar → 2kg;
- Batata → 3kg;
- Óleo → 5 litros;
- Bolacha de Água e Sal → 1 pacote;
- Bolacha de Maizena → 1 pacote;
- Banana → 1 dúzia e meia;
- Couve-Flor → 2 maços;
- Leite em Pó → 2 latas de 1kg;
→ Criar código em Python para inserir os preços por unidade de cada item das compras
e depois mostrar estes preços no console;
→ Calcular o preço total para cada item em função das quantidades, e mostrá-los no console;
→ Calcular o preço total da compra e mostrá-lo no console;
→ Estabelecer um limite de preço para o total da compra;
→ Se o preço da compra for inferior ao limite estabelecido imprimir no console:
    “pagamento em dinheiro”;
→ Se o preço da compra for superior ao limite estabelecido imprimir no console: 
    “pagamento em parcelas com uso de cartão”.

Created on Fri Aug 27 11:51:18 2021

@author: Renato
"""
# Entrada de preços dos produtos
arroz = float(input('Qual o preço do arroz (kg): R$ '))
qtde_arroz = float(input('Quantidade de arroz (kg): '))
feijão = float(input('Qual o preço do feijão (kg): R$ '))
qtde_feijão = float(input('Quantidade de feijão (kg): '))
açucar = float(input('Qual o preço do açucar (kg): R$ '))
qtde_açucar = float(input('Quantidade de açucar (kg): '))
batata = float(input('Qual o preço da batata (kg): R$ '))
qtde_batata = float(input('Quantidade de batata (kg): '))
óleo = float(input('Qual o preço do óleo (l): R$ '))
qtde_óleo = float(input('Quantidade de óleo (l): '))
bol_agua = float(input('Qual o preço da bolacha de água e sal (pacote): R$ '))
qtde_bol_agua = float(input('Quantidade de bolacha água e sal (pacote): '))
bol_maiz = float(input('Qual o preço da bolacha de maizena (pacote): R$ '))
qtde_bol_maiz = float(input('Quantidade de bolacha de maizena (pacote): '))
banana = float(input('Qual o preço da banana (dúzia): R$ '))
qtde_banana = float(input('Quantidade de banana (dúzia): '))
couve_flor = float(input('Qual o preço da couve-flor (maço): R$ '))
qtde_couve_flor = float(input('Quantidade de couve-flor (maço): '))
leite_po = float(input('Qual o preço do leite em pó (kg): R$ '))
qtde_leite_po = float(input('Quantidade de leite em pó (lata): '))
# Exibição no console com os cálculos por produto
print('Comprovante de Compra do Supermercado')
print('Produto\t\t\t\t\t\t      Qtde\t\tPreço\tSubtotal')
print(f'Arroz\t\t\t\t\t\t{qtde_arroz:10.1f}\t{arroz:9.2f}\t{qtde_arroz * arroz:7.2f}')
print(f'Feijão\t\t\t\t\t\t{qtde_feijão:10.1f}\t{feijão:9.2f}\t{qtde_feijão * feijão:7.2f}')
print(f'Açucar\t\t\t\t\t\t{qtde_açucar:10.1f}\t{açucar:9.2f}\t{qtde_açucar * açucar:7.2f}')
print(f'Batata\t\t\t\t\t\t{qtde_batata:10.1f}\t{batata:9.2f}\t{qtde_batata * batata:7.2f}')
print(f'Óleo\t\t\t\t\t\t{qtde_óleo:10.1f}\t{óleo:9.2f}\t{qtde_óleo * óleo:7.2f}')
print(f'Bolacha Água e Sal\t\t\t{qtde_bol_agua:10.1f}\t{bol_agua:9.2f}\t{qtde_bol_agua * bol_agua:7.2f}')
print(f'Bolacha de Maizena\t\t\t{qtde_bol_maiz:10.1f}\t{bol_maiz:9.2f}\t{qtde_bol_maiz * bol_maiz:7.2f}')
print(f'Banana\t\t\t\t\t\t{qtde_banana:10.1f}\t{banana:9.2f}\t{qtde_banana * banana:7.2f}')
print(f'Couve-flor\t\t\t\t\t{qtde_couve_flor:10.1f}\t{couve_flor:9.2f}\t{qtde_couve_flor * couve_flor:7.2f}')
print(f'Leite em pó\t\t\t\t\t{qtde_leite_po:10.1f}\t{leite_po:9.2f}\t{qtde_leite_po * leite_po:7.2f}')
print('-' * 60)
# Exibição e cálculo do total
total = qtde_arroz * arroz + qtde_feijão * feijão + qtde_açucar * açucar + qtde_batata * batata + qtde_óleo * óleo +\
        + qtde_bol_agua * bol_agua + qtde_bol_maiz * bol_maiz + qtde_banana * banana + qtde_couve_flor * couve_flor +\
        + qtde_leite_po * leite_po
print(f'Valor total da compra:\t\t\t\t\t\t\tR${total:9.2f}')
# Entrada e decisão da forma de pagamento
limite = float(input('Digite o valor limite da compra: R$ '))
if total < limite:
    print('Pagamento em dinheiro')
else:
    print('Pagamento em parcelas com uso do cartão')
