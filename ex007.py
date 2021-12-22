# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021
# Exercício 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

p1 = float(input('Digite a nota da 1ª Prova: '))
p2 = float(input('Digite a nota da 2ª Prova: '))

media = (p1 + p2) / 2

print('A média entre {:.1f} e {:.1f} resultou {:.1f}'.format(p1, p2, media))
