# Curso em Vídeo - Python - Mundo 1
# Data: 06/06/2021
# Exercício 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem em Km ? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O valor da passagem é R$ {:.2f}'.format(preco))

price = distancia * 0.50 if distancia <= 200 else distancia * 0.45      # condicional simplificada

print('O valor da passagem é R$ {:.2f}'.format(price))
