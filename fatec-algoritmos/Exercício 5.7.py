# Exercício 7:
# Construir código Python para multiplicar um número A por um número B (inteiros positivos) utilizando somas sucessivas.
# criado 2021 Sep 13
# author: Renato

a = int(input('Digite o primeiro número a multiplicar: '))
b = int(input('Digite o outro número: '))
k = produto = 0
while k < b:
    if a < 0 or b < 0:
        produto = 'ERRO'
        break
    produto += a
    k += 1
    print(f'{k} -> {produto}')
print(f'{a} x {b} = {produto}')
print('teste', produto == a * b)
