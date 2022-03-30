fila1 = []
# inserindo
print(fila1.inserir(1))
print(fila1.inserir(2))
print(fila1.inserir(3))
print(fila1.inserir(4))
print(fila1.inserir(5))
# imprimindo
for i in fila1:
    print(i, end=" -> ")
print('\b\b\b')
# imprimindo o que sobrou
for i in fila1:
    print(i, end=" -> ")
print("\b\b\b")
# inserindo
print(fila1.inserir(6))
print(fila1.inserir(7))
# imprimindo a fila atual
for i in fila1:
    print(i, end=" -> ")
print("\b\b\b")
