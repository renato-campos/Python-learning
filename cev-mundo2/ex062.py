print('Gerador de PA:')
termo1 = int(input('1º termo: '))
razao = int(input('Razão: '))
k = 0
qtdde = 10
print('PA =', end=' ')

while k < qtdde:
    termo = termo1 + k * razao
    k += 1
    print(termo, end=' -> ' if k < qtdde else ' PAUSA\n')
    if k == qtdde:
        qtdde += int(input('Quantos termos você quer mostrar mais? '))
print(f'Progressão finalizada com {qtdde} termos exibidos')
