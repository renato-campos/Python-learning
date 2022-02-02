nasc = input('Digite a data de nascimento DDMMAAAA: ')
digito = 0
while len(nasc) > 1:
    digito = 0
    for d in nasc:
        digito += int(d)
    nasc = str(digito)
print('Seu dígito da vida é', digito)
