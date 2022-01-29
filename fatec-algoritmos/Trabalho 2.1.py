# Exercício 1: Construir código em Python que possa calcular a média aritmética do aluno selecionado e
# retornar no console se o mesmo está aprovado (média >= 5.0) ou reprovado.
# Mostrar no console todas as notas do aluno selecionado → utilizar elif para selecionar o aluno.
#
# História 	Geografia 	Português 	Matemática 	Ciências 	Literatura 	Aluno
#   5.6 	    6.7 	    7.0 	    10.0 	    4.0 	    8.0 	Maria
#   2.3 	    6.6 	    8.0 	    5.5 	    10.0 	    5.0 	Tânia
#   7.7 	    4.0 	    7.0 	    7.9 	    2.2 	    6.5 	José
#   9.0 	    10.0 	    3.3 	    8.0 	    6.0 	    4.6 	Daniel

# Dados dos alunos
alunos = ['Maria', 'Tânia', 'José', 'Daniel']
historia = [5.6, 2.3, 7.7, 9.0]
geografia = [6.7, 6.6, 4.0, 10.0]
portugues = [7, 8, 7, 3.3]
matematica = [10, 5.5, 7.9, 8]
ciencias = [4, 10, 2.2, 6]
literatura = [8, 5, 6.5, 4.6]
# Entrada do nome do aluno
nome = input('Digite o nome do aluno: ')
# Seleção do Aluno
if nome == alunos[0]:
    k = 0
elif nome == alunos[1]:
    k = 1
elif nome == alunos[2]:
    k = 2
else:
    k = 3

# Cálculo da média e resultado
media = (historia[k] + geografia[k] + portugues[k] + matematica[k] + ciencias[k]) + literatura[k] / 6
if media >= 5:
    resultado = "APROVADO"
else:
    resultado = "REPROVADO"
# Exibição dos resultados
print(f'''Aluno:\t{alunos[k]}
História:\t{historia[k]:4.1f}
Geografia:\t{geografia[k]:4.1f}
Português:\t{portugues[k]:4.1f}
Matemática:\t{matematica[k]:4.1f}
Ciências:\t{ciencias[k]:4.1f}
Literatura:\t{literatura[k]:4.1f}
\nResultado: o aluno está {resultado} !''')
