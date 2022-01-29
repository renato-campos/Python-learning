# Exercício 2: Construir código Python que mostre no console a tabuada de soma e divisão de um número, utilizando o laço while.

# entrada da escolha
number = int(input('Tabuada da soma e da divisão de qual número: '))
print(f'\n Tabuada Soma\t|  Tabuada Divisão')
# Condição de existência da divisão
if number != 0:
    k = 0
else:
    k = 11
    print('\nNão existe Tabuada de Divisão do ZERO !')
# Cálculo e exibição das Tabuadas
while k <= 10:
    print(f'{number:2}  + {k:2} = {number + k:3}\t|  {(10 - k) * number:2}  / {number:2} = {(10 - k) * number / number:4.1f}')
    k += 1
print('\nFIM')
