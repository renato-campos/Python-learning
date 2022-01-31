# São um tipo de variável onde pode se armazenar vários valores, acessados por um índice
# Uma lista pode conter zero ou mais elementos de um mesmo tipo ou de vários tipos,
# além de poder ser composta por outras listas.
# O tamanho de uma lista é igual ao número de elementos que possui.

# declaração de uma lista vazia
lista = []
print(lista)

# iniciação de uma lista com 3 elementos
lista = [0, 33, 44]

# acesso aos elementos da lista através do índice
print(lista[0])
print(lista[1])
print(lista[2])

# manipulação dos elementos de uma lista
lista[0] = 22
print('valor atualizado de lista[0] =', lista[0])
lista[1] = lista[1] + lista[2]
lista[2] = lista[1] / 10
print('lista completa atual', lista)

# lista de caracteres
lista = ['a', 'e', 'i', 'o', 'u']
print('vogais', lista)

# lista de strings ou caracteres concatenados
lista = ['Aprendi', 'a ler', 'com a cartilha', 'Caminho Suave']
print('Onde você aprendeu a ler?', lista)
print('Onde você aprendeu a ler?', lista[0], lista[1], lista[2], lista[3])
