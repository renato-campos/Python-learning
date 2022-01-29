# Exercício 3:
# Construir código Python que mostre no console a tabuada de soma e divisão de um número.
# criado 2021 Sep 13
# author: Renato

k = 1
number = int(input('Tabuada da soma e da divisão de qual número: '))
print(f'\nTabuada Soma\t| Tabuada Divisão')
while k <= 10:
    print(f'{number:2}  + {k:2} = {number + k:3}\t|{number:2}  / {k:2} = {number / k:3.1f}')
    k += 1

