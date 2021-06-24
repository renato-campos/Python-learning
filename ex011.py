# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura em metros da parede: '))

area = largura * altura
tinta = area / 2

print('A quantia de tinta necessária será {:.1f} litros'.format(tinta))
