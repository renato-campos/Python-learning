print('Gerador de PA:')
termo1 = int(input('1º termo: '))
razao = int(input('Razão: '))
k = 0
print('PA = {', end=' ')
while k < 10:
    termo = termo1 + k * razao
    k += 1
    print(termo, end=', ' if k < 10 else ' }')
