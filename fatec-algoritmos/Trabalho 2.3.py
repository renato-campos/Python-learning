# Exercício 3: Dado um teste de múltipla escolha com cinco questões, onde cada questão vale 1 ponto e
# as respostas corretas são: questão 1 = C, questão 2 = D, questão 3 = B, questão 4 = A e questão 5 = E.
# Escrever código Python que leia a resposta de cada questão inserida por um usuário e
# retorne o total de pontos do mesmo. Utilizar o laço while.

nota = 0
k = 0
respostas = ['C', 'D', 'B', 'A', 'E']

while k <= 4:
    escolha = input(f'Digite a resposta da questão {k+1} [Letra Maiúscula]: ')
    if escolha == respostas[k]:
        nota = nota + 1
        print('Você Acertou essa questão')
    else:
        print('Você errou esta questão.')
    k = k + 1

print(f'\nVocê tirou nota {nota} !')
