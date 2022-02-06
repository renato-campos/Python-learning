# Python é uma linguagem ultra moderna, utilizada por grandes empresas como Google, YouTube, Industrial Light & Magic,
# Globo e muitas outras. Fácil de aprender, com código limpo e organizado, Python vem ganhando cada vez mais espaço,
# e chegou a sua hora de aprender. Curso criado pelo Prof. Gustavo Guanabara com uma temática divertida de vídeo-game
# para motivar seus alunos, é dividido em mundos para facilitar o estudo.
#
# O primeiro mundo foi pensando de forma a apresentar a linguagem ao aluno, o professor irá introduzir a linguagem,
# seus conceitos, montar o primeiro programa e ensinar alguns recursos básicos.

def pulalinha(c='*', n=80):
    print(c * n)


# Função print()

print('Olá, mundo!')

# Diferença entre Adição e Concatenação (+)

print(7 + 4)    # adição
print('7' + '4')    # Concatenação
print('Olá' + 'Mundo')
#print('7' + 4)  # Erro de Tipo

pulalinha()

# Print de variáveis

name = 'Renato'
idade = 47
peso = 110
print(name, idade, peso)
print(name, idade, peso, sep='***')
print(name, idade, peso, sep='\n', end='***')
print()

# Exercícios: 1, 2, 3
pulalinha()

# AULA 6
#
# Tipos primitivos no Python int() float() bool() e str()

n1 = input('Digite um número: ')
n2 = input('Digite mais um número: ')
s = n1 + n2
print('A soma vale', s, 'ops!')     # o que houve? pq?

pulalinha()

# Inteiro - int()

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma vale', s)
print(type(s))

pulalinha()

# Ponto flutuante = float()

n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
s = n1 + n2
print('A soma vale', s)
print(type(s))

pulalinha()

# bool() = Booleanos = True(!=0) False(=0 ou None)

print(bool(0))
print(bool(1))
print(type(bool(2)))
print(bool(2.5))
print(bool(None))

pulalinha()

# str() = String - texto

print(str(2.5))
print(str(5))
print(str(s))
print(str('olá'))
print(type('5.0'))

# code points e caracteres

char1 = 'a'
char2 = ' '   # espaço

# ord()   # toma um único caractere e retorna o seu code point
print(ord(char1))  # 97
print(ord(char2))  # 32

#chr()   # função toma um code point e devolve o seu caratere
print(chr(97))     # a
print('[' + chr(32) + ']')    # [ ] espaço

pulalinha()

# Métodos para Stings

n = input('Digite algo: ')
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.isascii())
print(n.isdecimal())
print(n.isdigit())
print(n.isidentifier())
print(n.isprintable())
print(n.isspace())
print(n.istitle())
print(n.isupper())
print(n.islower())

pulalinha()

# PRINT() DE STRING COM MÁSCARA

n1, n2, s = 2, 3, n1 + n2
print('A soma de {0} com {1} resulta {2}'.format(n1, n2, s))
print('A soma de {1} com {0} resulta {2}'.format(n1, n2, s))
print(f'A soma de {n1} com {n2} resulta {s}')

# Exercícios 3 (de novo) e 4
pulalinha()

# AULA 7 - OPERADORES ARITMÉTICOS
#
# + - * / // % **

print(5 + 2, 5.0 + 2.0, 5 + 2.0)
print(5 - 2, 5.0 - 2.0, 5 - 2.0)
print(5 * 2, 5.0 * 2.0, 5 * 2.0)
print(4 / 2, 4.0 / 2.0, 4 + 2.0)
print(5 // 2, 5.0 // 2.0, 5 // 2.0)
print(5 % 2, 5.0 % 2.0, 5 % 2.0)

pulalinha()

# Ordem de Precedência

print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)

pulalinha()

# ADIÇÃO OU CONCATENAR +
# MULTIPLICAR OU REPLICAR *

print('oi' + 'Renato')
print('=' * 20)

pulalinha()

# Formatação na máscara:
#
# {:20} tamanho do campo
# {:>20} alinhamento à direita
# {:<20} alinhamento à esquerda
# {:^20} alinhamento centralizado
# {:*^20} simbolo usado p/ preenchimento do restante do campo
# tem muito mais ...

name, idade = 'Renato', 47
print('olá {}'.format(name))
print('olá {:20}'.format(name))
print('olá {:>20}'.format(name))
print('olá {:<20}'.format(name))
print('olá {:^20}'.format(name))
print('olá {:=^20}'.format(name))
print('*' * 80)
print('olá {0}, você tem {1} anos'.format(name, idade))
print('olá {0:20}, você tem {1:>5.2f} anos'.format(name, idade))
print('olá {0:>20}, você tem {1:^10.3f} anos'.format(name, idade))
print('olá {0:<20}, você tem {1:#<15.1f} anos'.format(name, idade))
print('olá {0:^20}, você tem {1:.2f} anos'.format(name, idade))
print('olá {0:=^20}, você tem {1:*^10.0f} anos'.format(name, idade))

# Exercícios 5 ao 13
pulalinha()

# AULA 8: UTILIZANDO MÓDULOS
# Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos
# import e from/import no Python. Veja como carregar bibliotecas de funções e
# utilizar vários recursos adicionais nos seus programas utilizando
# módulos built-in e módulos externos, oferecidos no Pypi.

import math
from random import random

var = math.ceil(math.sqrt(random()))

# Exercícios 16 ao 21
pulalinha()

# Aula 9: Manipulando Cadeias de Texto

# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender
# são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(),
# lower(), capitalize(), title(), strip(), junção com join().

frase = 'Curso em Vídeo Python'

# Fatiamento
print(frase[9])
print(frase[9:13])  # perceba o fim do intervalo
print(frase[:5])
print(frase[15:])
print(frase[-6:])
print(frase[9:21:2])
print(frase[9::2])
print(frase[0:21])
print(frase[:])
print(frase[0:-1])
pulalinha()

# Análise

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))    # qual foi a resposta?
print('Curso' in frase)
print('Android' in frase)
print('Android' not in frase)
pulalinha()

# Transformação
# uma sting é como a tupla, imutável, mas esses métodos alteram a forma de saída.

print(frase.replace('Python', 'Android'))
frase.lower()
print(frase)    # apenas a saída do comando é alterada, a string permanece igual, imutável!
print(frase.upper())
print(frase.lower())
print(frase.title())
print(frase.capitalize())
print(frase.swapcase())
pulalinha()

# Divisão de string

print(frase.split())        # como a string é imutável, se você desejar salvar a modificação
teste = frase.split()       # você deve atualizar a variável redefinindo ela mesma ou em uma nova variável
print(teste)                # através de uma atribuição.
teste2 = '-'.join(teste)
print(frase, teste, teste2)
email = 'temujim@gmail.com'
email = email.split('@')
user, host = email[0], email[1]
print(email, user, host)

pulalinha()

frase = '   Aprenda Python   '

print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

# Exercícios 22 ao 27
pulalinha()

# Aula 10 - CONDIÇÕES

# Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
# Veja como aplicar os comandos if: e else: no Python.

nome = str(input('Qual o seu nome? '))          # condicional simples
if nome.title() == 'Renato':
    print('Que nome lindo!')
print('Olá', nome)


tempo = int(input('Quantos anos tem seu carro? ')) # condicional composta
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')

# TODA A CONDICIONAL EM APENAS UMA LINHA qdo simples, parecido com "operador ternário" de outras linguagens

print('Carro Novo') if tempo <=3 else print('Carro Velho')  #condicional simplificada

# Exercícios: 28 ao 35
pulalinha()

# AULA 11: Cores no Terminal

# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI
# para configurar cores para os seus programas em Python.
# Veja como utilizar o código \033[m com todas as suas principais possibilidades.

# veja também:
# módulo colorize
# https://realpython.com/lessons/ansi-escape-sequences/
# https://realpython.com/python-print/
# https://en.wikipedia.org/wiki/ANSI_escape_code

# O código ANSI de cores que funciona melhor para Python é o : \033[
# início =>         \033[       \033[
# estilo do texto:  código      0
# separação:        ;           ;
# texto:            código      33
# separação:        ;           ;
# côr do fundo:     código      44
# encerramento:     m           m

# resultado:        \033[0;33;44m

# Descrição dos Códigos que funcionam melhor em Python
# Estilo:                   Cores:                      Background:                 Exemplos:
#       0 nenhum            30 branco                   40 branco                   \033[0;30;41m
#       1 negrito           31 vermelho                 41 vermelho                 \033[4;33;44m
#       4 sublinhado        32 verde                    42 verde                    \033[1;35;43m
#       7 negativado        33 amarelo                  43 amarelo                  \033[30;42m
#                           34 azul                     44 azul                     \033[m
#                           35 roxo                     45 roxo                     \033[7;30m
#                           36 azul claro               46 azul claro
#                           37 cinza                    47 cinza

def esc(code):
    return f'\033[{code}m'


print('this is ', esc('31'), 'really', esc(0), ' important', sep='')
print('this is ', esc('31;1'), 'really', esc(0), ' important', sep='')
print('this is ', esc('31;1;4'), 'really', esc(0), ' important', sep='')

print('\033[4m\033[31m\033[43mRENATO GOMES DE CAMPOS\033[m e só')
