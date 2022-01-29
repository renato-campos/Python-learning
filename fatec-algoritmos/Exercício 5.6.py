# Exercício 6:
# Construir código Python faça a soma de n números inseridos pelo usuário.
# criado 2021 Sep 13
# author: Renato

n = int(input('Qunatos números irá somar: '))
soma = 0
k = 1
while k <= n:
    number = float(input('Digite um número a somar: '))
    soma += number
    k += 1
print('O total somado foi', soma)
