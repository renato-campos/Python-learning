# Curso em Vídeo - Python - Mundo 1
# Data: 05/06/2021
# Exercício 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).strip().title()
print('Existe "Silva" no nome: ', 'Silva' in nome)      # não funciona cpm Silvana, por exemplo

nome = nome.split()
print('A pessoa tem "Silva" no nome? ', str('Silva' in nome).replace('True', 'Sim, ela tem Silva no nome!')
      .replace('False', 'Não, elá não tem Silva no nome!'))
