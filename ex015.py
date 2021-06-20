# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 015:  Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dist_perc = float(input('Digite a quilometragem percorrida: '))
dias_rent = int(input('Quantidade de dias alugado: '))

valor = 60 * dias_rent + 0.15 * dist_perc

print('O valor total do aluguel: R${:>8.2f}'.format(valor))
