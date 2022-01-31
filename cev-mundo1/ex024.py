# Curso em Vídeo - Python - Mundo 1
# Data: 05/06/2021
# Exercício 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip().upper()

print('O nome da cidade começa com SANTO ?', cidade[0:5] == 'SANTO')

