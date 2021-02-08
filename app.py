from lib.arquivo import *
from lib.interface import *
from time import sleep
from os import system

# Verifcar existencia do arquivo de dados
dados = 'dados.txt'
if not verificar_arquvio(dados):
    criar_arquivo(dados)

while True:
    # Menu principal do sistema
    cabecalho('MENU PRINCIPAL')
    formatar_menu([
        'Ver dados gerados',
        'Gerar novos dados',
        'Sair do sistema'
    ])
    selecao = opcao_menu_principal()

    # Opção para exibir os dados gerados
    if selecao == 1:
        system('cls')
        cabecalho('DADOS GERADOS')
        ler_arquivo(dados)
        print(linha())
        input('Enter para continuar...')

    # Opção para gerar novos dados
    elif selecao == 2:
        system('cls')
        cabecalho('GERAR NOVOS DADOS')
        print('Escolha uma ou mais opções abaixo:')
        formatar_menu([
            'Nome',
            'E-mail',
            'Telefone',
            'Cidade',
            'Estado',
        ])
        opcao = opcao_cadastro()
        print('Gerando dados...')

        # Gerar dados da(s) opção(ões) selecionada(s)
        for item in opcao:
            sorteio = sortear_dados(item)
            gerar_dados(dados, sorteio)
        sleep(1)
        print('Dados gerados com sucesso.')

    # Opção para encerrar o sistema
    elif selecao == 3:
        system('cls')
        cabecalho('Saindo... Até a próxima.')
        sleep(1)
        system('cls')
        break

    # Mensagem caso o usuário escolha uma opção invalida
    else:
        print('Escolha uma opção válida.')

    system('cls')
    sleep(1)
