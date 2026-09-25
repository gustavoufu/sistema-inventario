from modelos import TITULO, VERDE, VERMELHO, NORMAL
from operacoes import (
    cadastrar_ativo,
    cadastrar_vulnerabilidade,
    listar_ativos,
    consultar_ativo,
    atualizar_ativo,
    remover_ativo)
from dados import carregar_ativos
from validacoes import verificar_int

lista_ativos = carregar_ativos()

while True:

    print()
    print(f"{TITULO}-=-=-=-=-=-=-= MENU PRINCIPAL =-=-=-=-=-=--=-={NORMAL}")
    print()
    print("1 - Cadastro de ativos")
    print("2 - Cadastrar vulnerabilidades")
    print("3 - Listar ativos")
    print("4 - Buscar e Consultar ativos")
    print("5 - Atualizar ativos")
    print("6 - Remover ativos")
    print("7 - Sair")
    print()

    opcao = verificar_int("Escolha uma opção: ")
    
    if opcao not in range(1, 8):
        print()
        print(f"{VERMELHO}ERRO: Essa opção não está disponível...{NORMAL}")
        continue

    elif opcao == 1:
        cadastrar_ativo(lista_ativos)

    elif opcao == 2:
        cadastrar_vulnerabilidade(lista_ativos)

    elif opcao == 3:
        listar_ativos(lista_ativos)

    elif opcao == 4:
        consultar_ativo(lista_ativos)

    elif opcao == 5:
        atualizar_ativo(lista_ativos)

    elif opcao == 6:
        remover_ativo(lista_ativos)

    elif opcao == 7:
        print()
        print(f"{VERDE}Saindo do sistema. Até logo!{NORMAL}")
        break
        