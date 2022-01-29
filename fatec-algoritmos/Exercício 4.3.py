# Exercício 3: Construir código em Python que possa ler 5 códigos de produtos e
# retornar no console o valor do preço do produto em função do código. Códigos e
# respectivos preços são dados na tabela a seguir:
# código  preço
# 1       13.30
# 2       1.40
# 3       19.00
# 4       123.79
# 5       44.33
# Created on Fri Sep 03 11:30:11 2021
# @author: Renato

# Entrada do código do produto
codigo = int(input('Digite o código do produto: '))
# Determinação do preço conforme o código entrado
if codigo == 1:
    price = 13.30
else:
    if codigo == 2:
        price = 1.40
    else:
        if codigo == 3:
            price = 19.00
        else:
            if codigo == 4:
                price = 123.79
            else:
                if codigo == 5:
                    price = 44.33
                else:
                    print('\n\033[1;41mERRO - Código deve estar entre 1 e 5\033[m')
                    price = 0
                    codigo = 'INVÁLIDO'
print(f'\nCódigo do Produto:\t{codigo:6}')
print(f'Preço do Produto:\tR${price:7.2f}')
