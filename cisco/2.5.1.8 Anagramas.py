text1 = input('Digite o 1º texto: ').upper()
text2 = input('Digite o 2º texto: ').upper()
comp1 = sorted(list(text1.replace(' ', '')))
comp2 = sorted(list(text2.replace(' ', '')))
if len(text2) == 0 or comp1 != comp2:
    print('Não são anagramas')
else:
    print('São anagramas')