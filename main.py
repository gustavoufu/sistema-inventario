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



try: #PEGA A ATUAL LISTA DE ATIVOS DO ARQUIVO JSON, SE NAO EXISTIR CRIA UMA LISTA VAZIA
    with open("arquivoativos.json", "r", encoding="utf-8") as arquivolista:
        lista_ativos = json.load(arquivolista)
except (FileNotFoundError, json.JSONDecodeError):
    lista_ativos = []


while True:  # EXIBE AS OPCOES DO CRUD 
    opcao = verificar_int("""
    -=-=-=-=-= OPÇÕES DE ATIVO =-=-=-=-=-=-

    1 - Cadastro de ativos
    2 - Listar ativos
    3 - Remover ativos
    4 - Atualizar ativos                     
    5 - Sair

    Escolha uma opção: """)

    if opcao not in range(1, 6):  # AVISA ERRO -> SE COLOCAR OPCAO QUE NAO EXISTE
        print("")
        print("ERRO: Essa opção não está disponível...")
        continue

    elif opcao == 1:  # COLETA DADOS DO NOVO ATIVO PARA SUBIR NA LISTA DE DICIONARIOS
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
        lista_ativos.append(dados_ativo_novo)
        print("")
        try:  # ARMAZENA A NOVA MODIFICACAO NO ARQUIVO COM A LISTA DE ATIVOS
            with open("arquivoativos.json", "w", encoding="utf-8") as arquivolista:
                json.dump(lista_ativos, arquivolista)
                print("Ativo cadastrado com sucesso!")
        except OSError:
            print("Não foi possível salvar os dados no arquivo.")

    elif opcao == 2:  # LISTA TODOS OS DICIONARIOS NA LISTA "LISTA_ATIVOS"
        print("-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-")
        print("")
        for ativo in lista_ativos:
            print(f"ID:{ativo['id']} - {ativo['nome']}")

    elif opcao == 3:  # EXIBE A LISTA DE ATIVOS CADASTRADOS PARA ESCOLHA DE REMOCAO DE ATIVO
        print("-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-")
        print("")
        print("Qual ativo você deseja remover?")
        print("")
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

    elif opcao == 4:
        ativo_escolhido = input("Digite o id do ativo: ")

    elif opcao == 5:
        break
