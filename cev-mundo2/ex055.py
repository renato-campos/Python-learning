maior = menor = 0
for i in range(5):
    peso = float(input(f'Digite o peso da {i+1}ª pessoa [kg]: '))
    if i == 0:
        maior = menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso foi de {maior}kg e o menor de {menor}kg')
