def verificarArquvio(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print(f'Erro ao tentar criar arquivo {nome}')


def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao tentar abrir o arquivo')
    else:
        for linha in arquivo:
            print(linha)
        arquivo.close()


def cadastrar(arq):
    try:
        arq = open(arq, 'at')
    except:
        pass
