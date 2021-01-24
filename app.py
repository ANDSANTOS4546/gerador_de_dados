from lib.interface import *
from time import sleep

while True:
    
    # Menu principal do sistema
    cabecalho('MENU PRINCIPAL')
    menuPrincipal([
        'Ver dados cadastrados',
        'Cadastrar novos dados',
        'Sair do sistema'
    ])
    sel = opcao_menu_principal()

    # Opção para exibir os dados cadastrados
    if sel == 1:
        pass

    # Opção para gerar novos dados
    elif sel == 2:
        cabecalho('CADASTRAR NOVOS DADOS')
        menuSecundario([
            'Nome',
            'E-mail',
            'Telefone',
            'Cidade',
            'Estado',
        ])
        sel2 = opcaoCadastro()

    # Opção para encerrar o sistema
    elif sel == 3:
        cabecalho('Saindo... Até a próxima.')
        sleep(1)
        break

    # Mensagem caso o usuário escolha uma opção invalida
    else:
        print('Escolha uma opção válida.')

    sleep(1)
