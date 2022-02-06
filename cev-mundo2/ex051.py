termo1 = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão desta PA: '))
print('Os 10 primeiros termos da PA: ', end=' {')
for i in range(10):
    termo = termo1 + razao * i          # calculando o termo no meio do loop
    print(termo, end=', ')
print('\b\b}')

termo10 = termo1 + 10 * razao
print('Os 10 primeiros termos da PA: ', end=' {')
for i in range(termo1, termo10, razao):     # termo final calculado antes e fazendo o loop calcular os intermediários
    print(i, end=', ')
print('\b\b}')
