num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
opcao = ''
while opcao != '5':
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = input('>>> Qual é a sua opção?')
    if opcao == '1':
        print(f'A soma de {num1} + {num2} é {num2 + num1}')
        print('*-' * 25)
    elif opcao == '2':
        print(f'A multiplicação de {num1} x {num2} é {num2 * num1}')
        print('*-' * 25)
    elif opcao == '3':
        print(f'A maior de {num1} e {num2} é {max(num1, num2)}')
        print('*-' * 25)
    elif opcao == '4':
        num1 = float(input('Digite um valor: '))
        num2 = float(input('Digite outro valor: '))
        print('*-' * 25)
    elif opcao == '5':
        print('Finalizando ...')
        print('*-' * 25)
    else:
        print('Opção incorreta')
        print('*-' * 25)
print('Fim do programa.')
