print('Números pares:', end=' ')
for k in range(2, 51, 2):       # melhor solução pois tem menos interações
    #print('.', end=' ')         # número de ptos representa cada iteração
    print(k, end=' ')
print('FIM')

for i in range(1, 51):           # usa mais processamento pelo maior número de iterações
    #print('.', end=' ')         # número de ptos representa uma iteração
    if i % 2 == 0:
        print(i, end=' ')
print('FIM')
