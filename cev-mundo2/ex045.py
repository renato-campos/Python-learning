import random, time
itens = ('Pedra', 'Papel', 'Tesoura')
print(f'''JOKENPÔ
Suas opções:
[0] {itens[0]}
[1] {itens[1]}
[2] {itens[2]}''')
user = int(input('Qual sua jogada? '))
machine = random.randint(0, 2)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ!!!')
time.sleep(0.5)
print('*-' * 30)
print(f'Computador jogou {itens[machine]}')
print(f'Usuário jogou {itens[user]}')
print('*-' * 30)
# resultado
if user == 0:
    if machine == 0:
        print('EMPATE')
    elif machine == 1:
        print('Computador Venceu')
    else:
        print('Jogador Venceu')
elif user == 1:
    if machine == 1:
        print('EMPATE')
    elif machine == 2:
        print('Computador Venceu')
    else:
        print('Jogador Venceu')
elif user == 2:
    if machine == 2:
        print('EMPATE')
    elif machine == 0:
        print('Computador Venceu')
    else:
        print('Jogador Venceu')
else:
    print('Jogador escolheu opção inválida\nO computador venceu')