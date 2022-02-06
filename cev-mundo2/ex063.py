qtdde = int(input('Quantos termos você quer mostrar? '))
k = 1
while k <= qtdde:
    if k == 1:
        n1 = 1
        print(n1, end=' -> ')
    elif k == 2:
        n2 = 1
        print(n2, end=' -> ')
    else:
        n1, n2 = n2, n1+n2
        print(n2, end=' -> ')
    k += 1
print('FIM')

