# O terceiro programa mostra um método simples que lhe permite introduzir uma linha cheia de números,
# e processá-los facilmente. Nota: a função de rotina input() , combinada juntamente com as funções int() ou float() ,
# é inadequada para esta finalidade.

def proc_number(line):
    number_line = line.split()
    total = 0
    if len(number_line) == 0:
        return 'Você não digitou número algum'
    for n in number_line:
        if n.isnumeric():
            total += float(n)
        else:
            print(n, 'não é um número')
    return total

line = input('Digite os números separados por espaço: ')
print(proc_number(line))
