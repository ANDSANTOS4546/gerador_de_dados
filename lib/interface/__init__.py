def linha(tam=40):
    """Gerar linha

    Args:
        tam (int, optional): tamanho da linha. Defaults to 40.

    Returns:
        str: linha com tamanho informado
    """
    tam = 50
    return '=' * tam


def cabecalho(msg):
    """Cabecalho formatado

    Args:
        msg (str): Texto centralizado
    """
    print(linha())
    print(msg.center(50))
    print(linha())


def leiaInt(msg):
    """Ler numeros inteiros

    Args:
        msg (str): Mensagem mostrada ao usuario

    Returns:
        int: valor inteiro
    """
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO! Por favor digite um valor inteiro válido.')
            continue
        else:
            return n


def menuPrincipal(lista):
    """Criar menu formatado sobre uma lista

    Args:
        lista (str): lista com as opcoes do menu
    """
    for pos, item in enumerate(lista):
        print(f'[{pos+1}] - {item}')
    print(linha())


def opcao_menu_principal():
    """Ler opcao informada pelo usuário

    Returns:
        int: Opcao informada
    """
    op = leiaInt('Sua opção: ')
    return op


def menuSecundario(lista):
    """Menu de geracao de cadastro

    Args:
        lista (str): Lista com as opcoes do sub menu
    """
    for pos, item in enumerate(lista):
        print(f'[{pos+1}] - {item}')
    print(linha())


def opcaoCadastro():
    """Ler opcao informada pelo usuário

    Returns:
        int : Opcao informada convertida para inteiro
    """
    args = str(input('Opção de cadastro: ')).split(',')
    for numero in args:
        return int(numero)


""" 
def dados(val):
    from random import choice

    nome = ['André', 'Anne', 'Fernando', 'Satoru', 'Rafael']
    email = ['andre@hotmail.com', 'anne@yahoo.com.br', 'fernando@outlook.com', 'satoru@gmail.com.br', 'rafael@bol.com']
    telefone = ['9 7858-9985', '9 5843-9416', '9 8573-2493', '9 8092-5482', '9 7543-5426']
    cidade = ['São Paulo', 'Barueri', 'Monte Alto', 'Ferraz de Vasconcelos', 'Guarulhos']
    estado = ['SP', 'SC', 'MG', 'RJ', 'PB']

    choice(val)
"""
