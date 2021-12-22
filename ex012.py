# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Digite o preço do produto: R$'))
price *= 0.95

print('O preço atual do produto com o desconto ficou R${:.2f}'.format(price))
