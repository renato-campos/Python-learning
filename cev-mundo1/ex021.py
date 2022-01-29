# Curso em Vídeo - Python - Mundo 1
# Data: 04/06/2021
# Exercício 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


import pygame.mixer     # após a instalação do pacote
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('Agora você escuta?')
