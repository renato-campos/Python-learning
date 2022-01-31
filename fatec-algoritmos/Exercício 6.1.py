# Exercício: Criar uma lista que corresponda aos cinco nomes completos de alunos da aula de Algoritmos e
# Introdução à Computação em sequência, criar lista para armazenar as respectivas idades destes alunos,
# e finalmente uma lista com as respectivas notas do 1º bimestre nesta disciplina.
# Imprimir no console os respectivos nomes ao lado das idades e das notas.

nomes = [input('Digite o nome do 1º aluno: '), input('Digite o nome do 2º aluno: '), input('Digite o nome do 3º aluno: '),
         input('Digite o nome do 4º aluno: '), input('Digite o nome do 5º aluno: ')]
idades = [int(input('Digite a idade do 1º aluno: ')), int(input('Digite a idade do 2º aluno: ')), int(input('Digite a idade do 3º aluno: ')),
         int(input('Digite a idade do 4º aluno: ')), int(input('Digite a idade do 5º aluno: '))]
notas = [float(input('Digite a nota do 1º aluno: ')), float(input('Digite a nota do 2º aluno: ')), float(input('Digite a nota do 3º aluno: ')),
         float(input('Digite a nota do 4º aluno: ')), float(input('Digite a nota do 5º aluno: '))]
'''
# Entrada no código para testes
nomes = ['Tony Stark', 'Steve Rogers', 'Stephen Strange', 'Bruce Banner', 'Peter Park']
idades = [10, 15, 12, 11, 7]
notas = [10.0, 5.5, 9.0, 9.5, 8]
'''
k = 0
print(f'Nome\t\t\t\t\t\t\t\t\tIdade\tNotas')
print('-' * 55)
while k < len(nomes):
    print(f'{nomes[k]:40}{idades[k]:4}\t{notas[k]:4.1f}')
    k += 1
