# Exercício 4: Criar uma lista que corresponda aos cinco nomes completos de alunos da aula de Algoritmos e
# Introdução à Computação; em sequência, criar lista para armazenar as respectivas idades destes alunos, e
# finalmente uma lista com as respectivas notas do 1º bimestre nesta disciplina.
# Imprimir no console os respectivos nomes ao lado das idades e das notas.

nomes = ['Célia', 'Dyanna', 'Natália', 'Renato', 'Márcio']
idades = [30, 25, 35, 47, 60]
notas = [10, 9, 8, 7, 10]
k = 0
print('Nomes\tIdade\tNota')
print('-' * 20)
while k <= 4:
    print(f'{nomes[k]}\t{idades[k]:5}\t{notas[k]:4}')
    k = k + 1
