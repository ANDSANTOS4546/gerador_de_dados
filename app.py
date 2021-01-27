from lib.arquivo import *
from lib.interface import *
from time import sleep

# Verifcar existencia do arquivo de dados
dados = 'dados.txt'
if not verificarArquvio(dados):
    criarArquivo(dados)

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
        cabecalho('DADOS CADASTRADOS')
        lerArquivo(dados)
        print(linha())
        input('Enter para continuar...')
        
    # Opção para gerar novos dados
    elif sel == 2:
        cabecalho('CADASTRAR NOVOS DADOS')
        print('Escolha uma ou mais opções abaixo:')
        menuSecundario([
            'Nome',
            'E-mail',
            'Telefone',
            'Cidade',
            'Estado',
        ])
        op = opcaoCadastro()
        print('Gerando dados...')
        
        # Gerar dados da(s) opção(ões) selecionada(s)
        for item in op:
            sorteio = sortearDados(item)
            cadastrar(dados, sorteio)
        sleep(1)
        print('Dados gerados com sucesso.')
        
    # Opção para encerrar o sistema
    elif sel == 3:
        cabecalho('Saindo... Até a próxima.')
        sleep(1)
        break

    # Mensagem caso o usuário escolha uma opção invalida
    else:
        print('Escolha uma opção válida.')

    sleep(1)
