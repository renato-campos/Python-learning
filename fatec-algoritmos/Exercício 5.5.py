# Exercício 5:
# Construir código Python que confira uma senha pré # estabelecida com uma a ser inserida pelo usuário,
# que terá três tentativas para acertar.
# criado 2021 Sep 13
# author: Renato

tentativas = 0
password = 'senha123'
while tentativas < 3:
    if password == str(input('Digite a senha: ')):      # entrada e check da senha
        print('Senha correta - Login efetuado')
        break
    else:
        tentativas += 1
        print(f'ERRO - {tentativas}ª tentativa')
print('FIM')
