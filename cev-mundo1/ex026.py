# Curso em Vídeo - Python - Mundo 1
# Data: 05/06/2021
# Exercício 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite um texto qualquer: ')).strip().upper()

a_count = frase.count('A')
a_first = frase.find('A') + 1
a_last = len(frase) - frase[::-1].find('A')
a_last2 = frase.rfind('A') + 1

print('''A letra "A" aparece {} vezes no texto.
A primeira letra "A" aparece na {}ª posição.
A última letra "A" aparece na {}ª e {}ª posição.'''.format(a_count, a_first, a_last, a_last2))
