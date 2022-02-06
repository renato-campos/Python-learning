l1 = float(input('Digite a medida do 1º segmento: '))
l2 = float(input('Digite a medida do 2º segmento: '))
l3 = float(input('Digite a medida do 3º segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:      # condição de existência de triângulos
    print('Os segmentos podem formar um triângulo', end=' ')
    if l1 == l2 == l3:
        print('equilátero.')
    elif l1 != l2 != l3 != l1:
        print('escaleno.')
    else:                                   # (l1==l2 and l1 != l3) or (l1==l3 and l1!=l2) or (l2==l3 and l2!=l1) ...
        print('isóceles.')                  # ... ou l1==l2!=l3 or l1!=l2==l3 or l1==l3!=l2
else:
    print('Os segmentos não podem formar um triângulo.')
