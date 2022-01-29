# Exercício 4:
# Construir código Python que mostre no console incrementos numéricos,
# a partir de 0, até que seja digitado a palavra “parar”.
# criado 2021 Sep 13
# author: Renato

flag = 'continuar'
k = 0
while flag != 'parar':
    print(k)
    flag = str(input('Digite parar para interromper a contagem: '))
    k += 1
print('FIM')