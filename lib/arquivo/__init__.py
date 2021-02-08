def verificar_arquvio(nome):
    """Verificar existencia do Arquivo

    Args:
        nome (str): nome do arquivo

    Returns:
        bool: True or False
    """
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """Criar o arquivo txt

    Args:
        nome (str): Nome que sera atribuido ao arquivo txt
    """
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print(f'Erro ao tentar criar arquivo {nome}')


def ler_arquivo(nome):
    """Ler o arquivo txt criado

    Args:
        nome (str): Nome do arquivo txt criado
    """
    try:
        arquivo = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao tentar abrir o arquivo')
    else:
        for linha in arquivo:
            print(linha, end='')
        arquivo.close()


def gerar_dados(nome, valor):
    """Inserir valores gerados no arquivo informado

    Args:
        nome (str): Nome do arquivo txt
        valor (str): Dado que sera escrito no arquivo
    """
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
