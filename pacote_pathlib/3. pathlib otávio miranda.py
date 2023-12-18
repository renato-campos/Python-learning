from pathlib import Path

def linha():
    print('\n'+'-'* 80 + '\n')


linha()

caminho_projeto = Path()
print(caminho_projeto)
print(caminho_projeto.absolute(), '<')
print(Path.cwd(), '<<')

linha()

caminho_arquivo = Path(__file__)    # não funciona em ipynb
print(caminho_arquivo)
print(caminho_arquivo.absolute())

linha()

print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)
linha()

ideias = caminho_projeto / 'pasta_0'
print(ideias)
print(ideias.absolute())
ideias1 = Path('pasta_0')
print(ideias1)
print(ideias1.absolute())
ideias2 = caminho_arquivo.parent.parent / 'pasta_0'
print(ideias2)
print(ideias2.absolute())
linha()

print(ideias == ideias1)
print(ideias == ideias2)
print(ideias.absolute() == ideias2)
print(ideias1 == ideias2)
linha()

print(ideias / 'teste.txt')
print(Path().home())            # pega o diretório padrão do usuário no sistema
linha()
# até agora todos esses caminhos eram apenas objetos na memória,
# nada efetivamente passado para o SO, mas vamos fazer isso agora
ideias.mkdir(exist_ok=True)                  # criando a pasta sem chamar o shutil
arquivo = 'teste.txt'
caminho_arquivo = ideias / arquivo      # criando o caminho para o local onde será criado o arquivo
caminho_arquivo.touch(exist_ok=True)                 # novamente sem o shutil
caminho_arquivo.write_text('Olá, mundo!', encoding='cp1252')
texto = caminho_arquivo.read_text()
print(texto)
#caminho_arquivo.unlink()        # apagando o arquivo
#ideias.rmdir()                  # apagando a pasta

linha()

# outra forma de trabalhar com edição de arquivo
ideias.mkdir(exist_ok=True)     # cria a pasta mas se existir não retorna erro
caminho_arquivo.touch(exist_ok=True)         # mesma coisa com o arquivo
with caminho_arquivo.open('+a') as arq:     # abre e fecha automaticamente o arquivo
    arq.write('uma linha\n')
    arq.write('outra linha\n')
print(caminho_arquivo.read_text())

linha()

for i in range(10):
    files = ideias / f'files{i}.txt'
    files.touch()
linha()
#ideias.rmdir()      # dá erro se a pasta não estiver vazia

# criar uma função para realizar um tipo de remove tree
def rmtree(raiz: Path, remove_raiz=True):
    for arquivo in raiz.glob('*'):      # busca todos os objetos no caminho
        if arquivo.is_dir():            # retorna True para diretórios
            print('Acessando pasta:', arquivo)
            rmtree(arquivo)
        else:                           # elif arquivo.is_file(): seria True para arquivo
            print('Apagando o arquivo:', arquivo)
            arquivo.unlink()
    raiz.rmdir()


#rmtree(ideias)

# LEMBRANDO QUE ISSO TUDO PODERIA SER REALIZADO APENAS IMPORTANDO
# A BIBLIOTECA SHUTIL E USANDO SUA FUNÇÃO RMTREE()
from shutil import rmtree

rmtree(ideias)

