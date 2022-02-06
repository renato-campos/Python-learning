soma = 0
for k in range(3, 501, 3):      # contagem só dos múltiplos de 3 - melhor solução, pois já divide as iterações por 3
    #print('.', end=' ')         # só para verificar o número de iterações
    if k % 2 == 1:              # seleciona só os ímpares
        soma += k
print('A soma dos valores é ', soma)

soma2 = 0
for i in range(1, 501, 2):      # contagem só dos ímpares
    #print('.', end=' ')         # só para verificar o número de iterações
    if i % 3 == 0:              # seleciona só os múltiplos de 3
        soma2 += i
print('A soma dos valores é ', soma2)
