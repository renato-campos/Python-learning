# Curso em Vídeo - Python - Mundo 1
# Data: 06/06/2021
# Exercício 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do veículo? '))

if velocidade > 80:
    print('Você voi Multado')
    multa = (velocidade - 80) * 7
    print('Valor da multa é de R$ {:.2f}'.format(multa))
else:
    print('Velocidade legal!')
print('Dirija com segurança !')