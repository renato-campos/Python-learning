# Aula 06 - Explicando melhor as f-strings

nome = 'Renato'
print(f'Bom dia, {nome} !')

# exemplo formatando o valor numérico com 6 espaços depois de “ “::” e 2 caracteres após o ponto decimal:
price = 10.98
print(f'valor do quilo do feijão R$ {price:6.2f}...tá caro')

# formatando o valor numérico com 10 espaços depois de : e 2 caracteres após o ponto decimal:
price = 12.98
print(f'valor do quilo do feijão R$ {price:10.2f}...estava caro, aumentou?!')
print('*' * 40)
# Uso de “ > ” para alinhar impressão à direita
price = 11.98
produto = 'Feijão'
print(f'valor do quilo do feijão R$ {price:20.2f}...tá caro')        # com número o alinhamento default é à direita
print(f'valor do quilo do feijão R$ {price:>20.2f}...tá caro')       # > desnecessário
print(f'quilo do {produto:20}...tá caro')                            # com string o alinhamento default é à esquerda
print(f'quilo do {produto:>20}...tá caro')                           # > necessário
print('*' * 40)
# Uso de “ < ” para alinhar impressão à esquerda
price = 11.98
produto = 'Feijão'
print(f'valor do quilo do feijão R$ {price:20.2f}...tá caro')        # com número o alinhamento default é à direita
print(f'valor do quilo do feijão R$ {price:<20.2f}...tá caro')       # < necessário
print(f'quilo do {produto:25}...tá caro')                            # com string o alinhamento default é à esquerda
print(f'quilo do {produto:<25}...tá caro')                           # < desnecessário
print('*' * 40)
# Uso de “ ^ ” para alinhar impressão centralizada
price = 11.98
produto = 'Feijão'
print(f'valor do quilo do feijão R$ {price:20.2f} ...tá caro')        # com número o alinhamento default é à direita
print(f'valor do quilo do feijão R$ {price:^20.2f} ...tá caro')       # ^ necessário
print(f'quilo do {produto:25} ...tá caro')                            # com string o alinhamento default é à esquerda
print(f'quilo do {produto:^25} ...tá caro')                           # ^ necessário
print('*' * 40)
print(f'valor do quilo do feijão R$ {price:.>20.2f} ...tá caro')
print(f'quilo do {produto:_>20} ...tá caro')
print(f'valor do quilo do feijão R$ {price:*<20.2f} ...tá caro')
print(f'valor do quilo do feijão R$ {price:-^20.2f} ...tá caro')
print(f'quilo do {produto:#<25} ...tá caro')
print(f'quilo do {produto:=^25} ...tá caro')
print('*' * 40)
# chamando funções com f-strings, convertendo para inteiro com f strings
número = 5.7
print(f'valor do número inteiro = {int(número)}\tconversão de 5.7 para inteiro')
número = 8
print(f'valor do número float = {float(número)}\tconversão de 8 para float')
print(f'(8*3)+4.532 = {float((número*3)+4.532):#<10.3f}')
