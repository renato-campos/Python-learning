# Curso em Vídeo - Python - Mundo 1
# Data: 06/06/2021
# Exercício 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)                                                           # sorteio do número pelo pc
print('-=*=-' * 10)
print('Vou escolher um número de 0 a 5, tente adivinhar!')
print('-=*=-' * 10)
print()
usuario = int(input('Em qual número eu pensei ... '))                                # entrada da escolha do usuário
print('Analisando . . .')
sleep(2)
if computador == usuario:                                                            # verificação do resultado
    print(f'PARABÉNS, VOCÊ ACERTOU O NÚMERO {computador}!')                          # se acertou
else:
    print(f'Você errou, era o número {computador}, mais sorte na próxima.')          # se errou
print('---Fim de Jogo---')
