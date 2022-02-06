# Curso em Vídeo - Python - Mundo 1
# Data: 03/06/2021 rev 02/02/2022
# Exercício 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número inteiro: '))

ante = numero - 1
suce = numero + 1

print('O número {} tem como antecessor o {} e o {} como sucessor.'.format(numero, ante, suce))
print(f'O número {numero} tem antecessor o {ante} e como sucessor o {suce}')
