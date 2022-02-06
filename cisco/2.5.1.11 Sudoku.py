def checagem(digitos):
    return sorted(list(digitos)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']


sudoku_linhas = ['295743861', '431865927', '876192543', '387459216', '612387495', '549216738',
                 '763524189', '928671354', '154938672']
sudoku_colunas = ['248365791', '937814625', '516729384', '781432569', '469581273', '352976418',
                  '895247136', '624193857', '173658942']
sudoku_subquad = []
# for i in range(9):
#    linha = input(f'Digite a {i+1}ª linha: ')
#    sudoku_linhas.append(linha)
# print(sudoku_linhas)
resp = True
for d in range(9):
    resp = checagem(sudoku_linhas[d])
    if not resp:
        break
print(resp)
# for k in range(9):
#    coluna = ''
#    for linha in sudoku_linhas:
#        coluna += linha[k]
#    sudoku_colunas.append(coluna)
# print(sudoku_colunas)
