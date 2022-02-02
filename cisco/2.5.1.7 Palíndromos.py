texto = input('Digite o texto: ').upper()
texto = texto.replace(' ', '')
pali = list(texto)
pali.reverse()
pali = ''.join(pali)
print(pali)
if pali != texto or len(texto) == 0:
    print('Não é um palíndromo')
else:
    print('É um palíndromo')
