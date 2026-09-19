import json
from enum import Enum

class TiposDeAtivos(Enum):
    Notebook = 1
    Servidor = 2
    Roteador = 3
    Aplicativo = 4


def verificar_int(mensagem):  # VERIFICAR INT É LIGADO A UMA MENSAGEM INPUT
    while True:
        try:
            inteiro = int(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO, digite um número inteiro válido...")
            continue
        else:
            return inteiro


def pedir_nome(): #PEDE O NOME DO ATIVO E VERIFICA SE É VAZIO
    while True:
        nome = input("Digite o nome do ativo: ").strip()
        if nome == "":
            print("ERRO, digite um nome válido...")
            continue
        else:
            return nome


def pedir_responsavel():  # PEDE O RESPONSAVEL E VERIFICA SE É VAZIO
    while True:
        responsavel = input("Digite o responsável pelo ativo: ").strip()
        if responsavel == "":
            print("ERRO, digite um nome válido...")
            continue
        else:
            return responsavel


def pedir_setor():  # PEDE O SETOR E VERIFICA SE É VAZIO
    while True:
        setor = input("Digite o setor responsável: ").strip()
        if setor == "":
            print("ERRO, digite um nome válido...")
            continue
        else:
            return setor


def pedir_severidade():  # PEDE A SEVERIDADE E VERIFICA SE É NUMERO INTEIRO DE 1 A 4
    while True:
        try:
            severidade = int(input("Digite um nível de severidade [1 até 4]: "))
            if severidade not in range(1, 5):
                print("O número digitado não é um valor de 1 a 4")
                continue
        except (ValueError, TypeError):
            print("ERRO, digite um número inteiro válido...")
            continue
        else:
            return severidade


def exibir_tipos_de_ativos():  # EXIBE OS TIPOS DE ATIVOS DISPONIVEIS
    print("-=-=-=-=- Tipos de ativos disponíveis -=-=-=-=-")
    for tipo in TiposDeAtivos:
        print(f"{tipo.value} - {tipo.name}")


def pedir_tipo_de_ativo():  # PEDE O TIPO DE ATIVO E VERIFICA SE É NUMERO INTEIRO DE 1 A 4
    while True:
        try:
            tipo = int(input(f"Digite o tipo do ativo [1 até {len(TiposDeAtivos)}]: "))
            if tipo not in range(1, len(TiposDeAtivos) + 1):
                print(f"O número digitado não é um valor de 1 a {len(TiposDeAtivos)}")
                continue
        except (ValueError, TypeError):
            print("ERRO, digite um número inteiro válido...")
            continue
        else:
            return tipo



try: #LEITURA DO JSON INICIAL PARA CARREGAR A LISTA DE ATIVOS CADASTRADOS
    with open("arquivoativos.json", "r", encoding="utf-8") as arquivolista:
        lista_ativos = json.load(arquivolista)
except (FileNotFoundError, json.JSONDecodeError):
    lista_ativos = []


while True:  # EXIBE AS OPÇÕES DO CRUD
    opcao = verificar_int("""
-=-=-=-=-=-=-= MENU PRINCIPAL =-=-=-=-=-=--=-=

1 - Cadastro de ativos
2 - Listar ativos
3 - Buscar e Consultar ativos
4 - Remover ativos
5 - Sair

Escolha uma opção: """)
    
    if opcao not in range(1, 6):  # AVISA ERRO -> SE COLOCAR OPCAO QUE NAO EXISTE
        print("")
        print("ERRO: Essa opção não está disponível...")
        continue

    elif opcao == 1:  # CADASTRO DE NOVO ATIVO
        print("")
        print("-=-=-=-=-=- CADASTRO DE NOVO ATIVO -=-=-=-=-=-=-")
        print("")
        if lista_ativos:
            novo_id = max(ativo["id"] for ativo in lista_ativos) + 1
        else:
            novo_id = 1

        dados_ativo_novo = { #CADASTRO DE NOVO ATIVO COM DICIONARIO
            "id": novo_id,
            "nome": pedir_nome(),
            "responsavel": pedir_responsavel(),
            "setor": pedir_setor(),
            "tipo": exibir_tipos_de_ativos() or pedir_tipo_de_ativo(),
            "vulnerabilidades": [],
        }
        print("")
        lista_ativos.append(dados_ativo_novo)

        try:  # ARMAZENA A NOVA MODIFICACAO NO ARQUIVO COM A LISTA DE ATIVOS
            with open("arquivoativos.json", "w", encoding="utf-8") as arquivolista:
                json.dump(lista_ativos, arquivolista)
                print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    Ativo cadastrado com sucesso!""")
        except OSError:
            print("Não foi possível salvar os dados no arquivo.")

    elif opcao == 2:  # LISTAGEM DE ATIVOS CADASTRADOS
        print("")
        if lista_ativos == []:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("")
            print("Não há ativos cadastrados!")
            continue
        else:
            print("-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-")
            print("")
            for ativo in lista_ativos:
                print(f"ID:{ativo['id']} - {ativo['nome']}")

    elif opcao == 3: # BUSCA E CONSULTA DE ATIVOS
        print("""
    -=-=-=-=-=- OPÇÕES =-=-=-=-=-=-

    1 - Buscar por ID
    2 - Buscar por Nome
    3 - Voltar ao menu principal
    """)
        
        while True:
            busca_opcao = verificar_int("Escolha uma opção: ")
            if busca_opcao not in range(1, 4):
                print("Essa opção não está disponível, Tente novamente!")
                continue
            else: break

        if busca_opcao == 1:
            id_digitado = verificar_int("Digite o ID do ativo que deseja buscar: ")
            print("")
            if id_digitado not in [ativo["id"] for ativo in lista_ativos]:
                print("")
                print("Esse ID não foi encontrado!")
                continue
            else:
                for ativo in lista_ativos:
                    if ativo["id"] == id_digitado:
                        print("-=-=-=-=-=- ATIVO ENCONTRADO -=-=-=-=-=-=-")
                        print(f"ID: {ativo['id']}")
                        print(f"Nome: {ativo['nome']}")
                        print(f"Responsável: {ativo['responsavel']}")
                        print(f"Setor: {ativo['setor']}")
                        print(f"Tipo: {TiposDeAtivos(ativo['tipo']).name}") 
                        # essa parte caça dentro do dicionario "ativo" o valor da key "tipo",
                        # manda o valor pra enumeracao e procura o nome para tal valor
                        print(f"Vulnerabilidades: {ativo['vulnerabilidades']}")

        elif busca_opcao == 2: 
            nome_digitado = input("Digite o nome do ativo que deseja buscar: ").strip()
            encontrado = False
            # encontrado false serve para, caso nao seja encontrado o nome do ativo, continue false e assim possa rodar o print 
            # de aviso "nao encontrado"
            for ativo in lista_ativos:
                if ativo["nome"].lower() == nome_digitado.lower():
                    # os lower() é só pra garantir que ambos textos estejam minusculos, ou seja, iguais
                    print("-=-=-=-=-=- ATIVO ENCONTRADO -=-=-=-=-=-=-")
                    print(f"ID: {ativo['id']}")
                    print(f"Nome: {ativo['nome']}")
                    print(f"Responsável: {ativo['responsavel']}")
                    print(f"Setor: {ativo['setor']}")
                    print(f"Tipo: {TiposDeAtivos(ativo['tipo']).name}") 
                    # essa parte caça dentro do dicionario "ativo" o valor da key "tipo",
                    # manda o valor pra enumeracao e procura o nome para tal valor
                    print(f"Vulnerabilidades: {ativo['vulnerabilidades']}")
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    encontrado = True
            if not encontrado:
                print("Esse nome não foi encontrado!")

        if busca_opcao == 3:
            continue

    elif opcao == 4:  #REMOÇÃO DE ATIVOS
        if lista_ativos == []:
            print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    
    Não há ativos cadastrados!""")
            continue
        
        print("""
-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-

Qual ativo você deseja remover?
    """)
        for ativo in lista_ativos:
            print(f"ID:{ativo['id']} - {ativo['nome']}")
        print("")

        while True:  # CRIA UM LOOP PARA SELECIONAR UM ID DE ATIVO VALIDA PARA EXCLUIR
            escolha_rem = verificar_int("Digite o ID do ativo a ser removido: ")
            
            encontrado = False
            for ativo in lista_ativos:
                if ativo["id"] == escolha_rem:
                    lista_ativos.remove(ativo)
                    encontrado = True
                    print("")
                    print("Ativo removido!")
                    break

            if not encontrado:
                print("Esse ID não foi encontrado!")

            try:  # ARMAZENA A NOVA MODIFICACAO NO ARQUIVO COM A LISTA DE ATIVOS
                with open("arquivoativos.json", "w", encoding="utf-8") as arquivolista:
                    json.dump(lista_ativos, arquivolista)
            except OSError:
                print("Não foi possível salvar os dados no arquivo.")
            break

    elif opcao == 5: #SAIR DO PROGRAMA
        break
        