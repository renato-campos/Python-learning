number = int(input('Digite um número: '))
div = 0
for i in range(1, number+1):
    if number % i == 0:
        div += 1
        print(f'\033[1;32m{i}\033[m', end=' ')
    else:
        print(f'\033[1;31m{i}\033[m', end=' ')

if div == 2:
    print(f'\nO número {number} é PRIMO.')
else:
    print(f'\nO número {number} não é primo.')
