import random
sorteio = random.randint(0, 10)
user = ''
tentativas = 0
print('''Sou seu computador...
Acabei de sortear um número entre 0 e 10
Você consegue acertar?''')
while sorteio != user:      # poderia ter usado um flag
    user = int(input('Qual sua escolha? '))
    tentativas += 1
    if user < sorteio:
        print('Maior ... tente outra vez')
    elif user > sorteio:
        print('Menor... tente novamente')
    else:
        print(f'Parabéns, acertou com {tentativas} tentativas')
