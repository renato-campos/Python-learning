# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.

real = float(input('Digite o valor em Reais para câmbio: R$ '))

cot_us, cot_eu = 5.08, 6.16

print('Os R${} podem ser trocados por U${:.2f} ou ${:.2f} euros'.format(real, real / cot_us, real / cot_eu))
