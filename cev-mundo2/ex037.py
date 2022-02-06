# entrada de dados
number = int(input('Digite o número a converter: '))        # posso usar um try
# menu de seleção
escolha = int(input('''Escolha a base para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal
-> Qual a sua escolha: '''))
# conversão
if escolha == '1':
    print(f'{number} em BINÁRIO é {bin(number)[2:]}')
elif escolha == '2':
    print(f'{number} em OCTAL é {oct(number)[2:]}')
elif escolha == '3':
    print(f'{number} em HEXADECIMAL é {hex(number)[2:].upper()}')
else:
    print('Seleção inválida.')
