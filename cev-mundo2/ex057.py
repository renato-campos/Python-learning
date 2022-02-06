sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0]
while sexo not in 'FM':
    sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0]
print(f'O sexo informado foi {sexo}')