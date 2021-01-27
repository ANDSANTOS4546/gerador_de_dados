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
            print(linha, end='')
        arquivo.close()


def cadastrar(nome, valor):
    try:
        arquivo = open(nome, 'at', encoding="utf-8")
    except:
        print('Erro ao tentar ler arquivo')
    else:
        try:
            arquivo.write(f'{valor}\n')
        except:
            print('Erro ao tentar escrever arquivo')
        else:
            arquivo.close()