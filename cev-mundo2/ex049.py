number = int(input('Digite o número: '))
print(f'\nTabuada do {number}')
print('-' * 15)
for i in range(11):
    print(f'{i} x {number} = {i * number}')
