# Exemplo de uso deo Laço de Repetição - while
# criado dia 2021 Sep 10
# author: Renato

# Iniciando o contador
k = 0
# Entrada do limite
limite = int(input('Digite até qual número exibir: '))
# laço de repetição
while k <= limite:
    if k % 2 == 0:
        print(k, end=' - ')
    k += 1                  # incremento do contador, poderia somar 2 e já pular os ímpares
print('FIM')
