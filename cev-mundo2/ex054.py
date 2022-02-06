import datetime as dt
maiores = menores = 0
for k in range(7):
    nasc = int(input(f'Digite o ano de nascimento da {k+1}ª pessoa: '))
    if dt.datetime.today().year - nasc >= 21:       # maioridade considerada 21 anos
        maiores += 1
    else:
        menores += 1
print(f'Das pessoas {maiores} são maiores de idade e {menores} são menores.')
