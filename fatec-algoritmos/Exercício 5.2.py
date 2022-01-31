# Exercício 2:
# Construir código Python que mostre no console a tabuada
# de multiplicação de um número.
# criado dia 2021 Sep 10
# author: Renato

# iniciando o contador
k = 0
# seleção da tabuada
number = int(input("Tabuada de qual número: "))
print('\nTabuada do', number)
print("-"*14)
# laço de repetição
while k <= 10:
    print(f'{number:2}  x {k:2} = {number * k:3}')
    k += 1

