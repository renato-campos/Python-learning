# Exercício 1:
# Construir código Python que mostre no console os números # ímpares dentro de um limite inserido pelo usuário.
# criado dia 2021 Sep 10
# author: Renato

# iniciando o contador
k = 0                           # poderia iniciar direto no 1, primeiro ímpar
# entrada do limite de contagem
limite = int(input('Digite até quanto contar: '))
# Laço de repetição
while k <= limite:
    if k % 2:                   # Condição dos ímpares
        print(k, end=' - ')
    k += 1                      # incremento do contador, novamente poderia pular de 2 em 2
print('FIM')
