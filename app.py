from lib.arquivo import *
from lib.interface import *
from time import sleep
from os import system

# Verifcar existencia do arquivo de dados
dados = 'dados.txt'
if not verificarArquvio(dados):
    criarArquivo(dados)

while True:
    # Menu principal do sistema
    cabecalho('MENU PRINCIPAL')
    formatarMenu([
        'Ver dados gerados',
        'Gerar novos dados',
        'Sair do sistema'
    ])
    selecao = opcao_menu_principal()

    # Opção para exibir os dados gerados
    if selecao == 1:
        system('cls')
        cabecalho('DADOS GERADOS')
        lerArquivo(dados)
        print(linha())
        input('Enter para continuar...')

    # Opção para gerar novos dados
    elif selecao == 2:
        system('cls')
        cabecalho('GERAR NOVOS DADOS')
        print('Escolha uma ou mais opções abaixo:')
        formatarMenu([
            'Nome',
            'E-mail',
            'Telefone',
            'Cidade',
            'Estado',
        ])
        opcao = opcaoCadastro()
        print('Gerando dados...')

        # Gerar dados da(s) opção(ões) selecionada(s)
        for item in opcao:
            sorteio = sortearDados(item)
            gerar(dados, sorteio)
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
