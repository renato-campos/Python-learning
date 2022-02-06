soma_par = 0
for i in range(6):
    number = int(input('Digite um número: '))
    if number % 2 == 0:
        soma_par += number
    else:
        print('Desconsiderado')
print(f'O valor total da soma dos pares é {soma_par}')
