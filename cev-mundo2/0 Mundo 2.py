# O segundo mundo apresenta as estruturas de repetição, muito importantes para qualquer linguagem,
# o professor explica sobre os comandos if, else, for e while e suas usabilidades.

def pulalinha(x='*', n=80):
    print(x * n)


# AULA 12 :  ESTRUTURAS DE CONTROLE - CONDICIONAIS ANINHADAS

# Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
# usando os comandos if.. elif.. else em programas Python.

nome = str(input('Qual o seu nome? '))

# condicional simples
if nome.title() == 'Renato':
    print('Que nome bonito!')
print('Tenha um bom dia, {}'.format(nome.title()))

pulalinha()

# condicional composta
if nome.title() == 'Renato':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome.title()))

pulalinha()

# condicional simplificada
print('Que nome bonito!') if nome.title() == 'Renato' else print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome.title()))

pulalinha()

# condicional aninhada
if nome.title() == 'Renato':
    print('Que nome bonito!')
else:
    if nome.title() == 'Lucas':
        print('Seu nome é bem popular no Brasil')
    else:
        print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome.title()))
pulalinha()

# condicional aninhada em Python
if nome.title() == 'Renato':
    print('Que nome bonito!')
elif nome.title() == 'Lucas':
    print('Seu nome é bem popular no Brasil')
elif nome.title() == 'Ana':
    print('Que belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome.title()))

# Exercícios: 36 ao 45
pulalinha()

# AULA 13: Nessa aula, vamos começar nossos estudos com os laços de repetições/iterações e vamos fazer primeiro o “for”,
# que é uma estrutura versátil e simples de entender. Por exemplo:
# no caso do 'for' é chamado de VARIÁVEL DE CONTROLE, ele é ideal para iterar sobre alguma estrutura ou quando você
# sabe o número de iterações que deverão ser efetuadas 
for c in range(0, 4):
    print(c)
print('Acabou')

pulalinha()

for c in range(0, 4):
    print(c)
    print('Acabou')

pulalinha()
for c in range(1, 5):
    print(c)
print('Acabou')
pulalinha()
for c in range(5, 0, -1):
    print(c)
print('Acabou')
pulalinha()
for c in range(0, 10, 2):
    print(c)
print('Acabou')
pulalinha()
inicio = int(input('Digite um número de início: '))
fim = int(input('Digite o número final: '))
for c in range(inicio, fim + 1):
    print(c)
print('Acabou')

# Exercícios: 46 ao 56
pulalinha()


# Aula 14: Estrutura de repetição while

# Nessa aula, vamos continuar a estudar os laços e
# vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:
#
# c=1
# while c !=10:
#      print(c)
#      c+=1
# print('Acabou')

# diferença for para while
# sabendo o limite do range, vc pode escolher entre o for o while,
# mas se não souber, vc tem de usar o while

# for sabendo limite
for c in range(1, 10):
    print(c, end=' ')
print('Fim')
# while sabendo limite
c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('Fim')
# while não sabendo o limite vc usa o flag para finalizar,
# já no for não há possibilidade do flag
resp = 'S'
k = 0
while resp == 'S':
    print(k, end=' ')
    k += 1
    resp = str(input('Deseja continuar? S/N ')).strip().upper()
print('fim')
# vc pode usar até um break para finalizar antes do limite do range,
# mas vc não tem a opção de passar desse limite estabelecido logo no início do for
for k in range(1, 6):
    print(k, end=' ')
    resp = str(input('Deseja continuar? S/N ')).strip().upper()
    if resp == 'N':
        break
print('fim')
pulalinha()

# AULA 15: LOOPING INFINITOS E BREAK

k = 0
while True:
    k = int(input('Digite um número (0 para encerrar): '))
    if k == 0:
        break
    print(k, end=' ')
print('Fim')

pulalinha()
