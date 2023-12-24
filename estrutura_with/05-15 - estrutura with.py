# usado muito para arquivos

# sem with
# o open() abre o arquivo, se não existir também o cria
arquivo = open("meu_arquivo.txt", 'w')
# se der um bug na linha do write, ou em qualquer linha antes do close, vai dar cao
arquivo.write("Feito sem a estrutura 'with'")
arquivo.close()


# com with
# aqui, o with já lida com o abrir e fechar do arquivo, então ele não dá cao
with open("meu_arquivo.txt", 'w') as arquivo:
    arquivo.write("agora com a estrutura 'with' e write que sobrescreve")


with open("meu_arquivo.txt", 'a') as arquivo:
    arquivo.write("\nagora com a estrutura 'with' e append")


# pode usar para ler tb, sem problemas
with open("meu_arquivo.txt", 'r') as arquivo:
    print(arquivo.read())
