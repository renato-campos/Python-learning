import datetime
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = datetime.date.today().year - ano
if 0 <= idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:        # idade > 25
    categoria = 'MASTER'
# RESULTADO
print(f'O atleta tem {idade} e esta na categoria {categoria}')
