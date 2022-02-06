import datetime
ano_nasc = int(input('Digite seu anos de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc
if idade == 18:
    print('Você deve se alistar este ano.')
elif idade > 18:
    print(f'Seu ano de alistamento já passou a {idade - 18} anos')
else:
    print(f'Você se alistará em {18 - idade} anos')
