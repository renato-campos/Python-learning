# Curso em Vídeo - Python - Mundo 1
# Data: 04/06/2021
# Exercício 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

import random

print('A ordem de apresentação será: {}'.format(random.choices(alunos, k=4)))

random.shuffle(alunos)
print('A ordem de apresentação será: {}'.format(alunos))
