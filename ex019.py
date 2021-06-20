# Curso em Vídeo - Python - Mundo 1
# Data: 04/06/2021
# Exercício 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

import random

num = random.randint(0, 3)
print('O aluno escolhido foi {}'.format(alunos[num]))

escolhido = random.choice(alunos)
print('O aluno escolhido foi {}'.format(escolhido))

