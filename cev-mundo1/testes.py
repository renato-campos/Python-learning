texto = '''linha 1
linha 2'''

print(len(texto))

print(len('\t'))

print(ord('a'))

print(chr(67))

texto = 'tchau'
lista = list(texto)
print(texto, max(lista), max(texto), min(lista), min(texto))
print(lista.index('a'))
texto = 'tudo depende de você'
print(texto.capitalize())
print(texto.center(35, '*'))
print(texto.count('e'))
print('*'.join(lista))
print(texto.lower())
print(texto.upper())
print(texto.split(' '))
print(texto.swapcase())
print(texto.endswith('ce'))
print(texto.endswith('cê'))
print(texto.replace('você', 'Deus'))
print(texto)
