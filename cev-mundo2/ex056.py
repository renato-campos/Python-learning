media = 0
id_older = 0
older = '-'
mulheres20 = 0
for i in range(4):
    nome = input(f'Digite o nome da {i+1}ª pessoa: ').capitalize().strip()
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = input(f'Agora digite o sexo de {nome} [M/F]: ').strip().upper()[0]
    media += idade      # agregando as idades para depois calcularmos a média
    if older == '-' and sexo == 'M':
            id_older = idade
            older = nome
    if sexo == 'M' and idade > id_older:
            id_older = idade
            older = nome
    if sexo == 'F' and idade < 20:
            mulheres20 += 1
media /= 4      # agora sim usamos a idade já agregada e dividimos para termos a média
print(f'''A média de idade do grupo é de {media:.1f} anos,
{older} é o homem mais velho com {id_older} anos e
{mulheres20} mulheres têm menos de 20 anos.''')
