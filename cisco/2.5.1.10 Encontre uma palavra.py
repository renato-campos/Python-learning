word = input('Digite a palavra a buscar: ')
texto = input('Digite o texto onde buscar: ')
k = i = 0
for letter in word:
    k = texto.find(letter, k)
    if k == -1:
        print(f'A letra {letter} não localizada em {word}')
    else:
        print(f'A letra {letter} foi localizada na {k+1}ª posição')
        i += 1
if i == len(word):
    print(f'Todos os caracteres de {word} foram localizados dentro em {texto} em ordem')
else:
    print(f'Nem todos os caracteres de {word} foram localizados em {texto} em ordem')
