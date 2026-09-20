import json
from enum import Enum

class TiposDeAtivos(Enum):
    Notebook = 1
    Servidor = 2
    Roteador = 3
    Aplicativo = 4

class Severidade_Extenso(Enum):
    Baixa = 1
    Média = 2
    Alta = 3
    Crítica = 4

def salvar_arquivos(lista_ativos): #SALVA LISTA DE ATIVO NO ARQUIVO
    try:
        with open("arquivoativos.json", "w", encoding="utf-8") as arquivolista:
            json.dump(lista_ativos, arquivolista)
            return True
    except OSError:
        print("Não foi possível salvar no arquivo!")
        return False


def verificar_int(mensagem): # VERIFICAR INT É LIGADO A UMA MENSAGEM INPUT
    while True:
        try:
            inteiro = int(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO, digite um número inteiro válido...")
            continue
        else:
            return inteiro


def pedir_input(mensagem): # PEDE TEXTO E VERIFICA SE É VAZIO
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("ERRO, digite um texto válido...")
            continue
        else:
            return texto

        
def pedir_severidade(): # PEDE A SEVERIDADE E VERIFICA SE É NUMERO INTEIRO DE 1 A 4
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


def exibir_tipos_de_ativos(): # EXIBE OS TIPOS DE ATIVOS DISPONIVEIS
    print("")
    print("-=-=-=-=- TIPO DE ATIVOS DISPONÍVEIS -=-=-=-=-")
    print("")
    for tipo in TiposDeAtivos:
        print(f"{tipo.value} - {tipo.name}")


def pedir_tipo_de_ativo(): # PEDE O TIPO DE ATIVO E VERIFICA SE É NUMERO INTEIRO DE 1 A 4
    while True:
        try:
            print("")
            tipo = int(input(f"Digite o tipo do ativo [1 até {len(TiposDeAtivos)}]: "))
            if tipo not in range(1, len(TiposDeAtivos) + 1):
                print(f"O número digitado não é um valor de 1 a {len(TiposDeAtivos)}")
                continue
        except (ValueError, TypeError):
            print("ERRO, digite um número inteiro válido...")
            continue
        else:
            return tipo


def Exibe_Dados_ativo(ativo): # EXIBE OS DADOS DO ATIVO SELECIONADO
    print(f"ID: {ativo['id']}")
    print(f"Nome: {ativo['nome']}")
    print(f"Responsável: {ativo['responsavel']}")
    print(f"Setor: {ativo['setor']}")
    print(f"Tipo: {TiposDeAtivos(ativo['tipo']).name}") 
    # essa parte caça dentro do dicionario "ativo" o valor da key "tipo",
    # manda o valor pra enumeracao e procura o nome para tal valor


def Exibe_Vulnerabilidades_ativo(ativo): # EXIBE AS VULNERABILIDADES DO ATIVO SELECIONADO
    if len(ativo['vulnerabilidades']) == 0:
        print("Nenhuma vulnerabilidade cadastrada.")
    else:
        print(f"VULNERABILIDADES: ({len(ativo['vulnerabilidades'])})")
        print("")
        for posicao, vulnerabilidade in enumerate(ativo['vulnerabilidades'], start=1):
            print(f"{posicao}. Vulnerabilidade:")
            for chave, valor in vulnerabilidade.items():
                if chave == "severidade":
                    print(f"{chave.capitalize()}: {Severidade_Extenso(valor).name}")
                else:
                    print(f"{chave.capitalize()}: {valor}")
            print("")

try: #LEITURA DO JSON INICIAL PARA CARREGAR A LISTA DE ATIVOS CADASTRADOS E SETAR NA VARIAVEL GLOBAL "LISTA_ATIVO"
    with open("arquivoativos.json", "r", encoding="utf-8") as arquivolista:
        lista_ativos = json.load(arquivolista)
except (FileNotFoundError, json.JSONDecodeError):
    lista_ativos = []


while True:  # EXIBE AS OPÇÕES DO CRUD
    opcao = verificar_int("""
-=-=-=-=-=-=-= MENU PRINCIPAL =-=-=-=-=-=--=-=

1 - Cadastro de ativos
2 - Cadastrar vulnerabilidades
3 - Listar ativos
4 - Buscar e Consultar ativos
5 - Atualizar ativos
6 - Remover ativos
7 - Sair

Escolha uma opção: """)
    
    if opcao not in range(1, 8):  # AVISA ERRO -> SE COLOCAR OPCAO QUE NAO EXISTE
        print("")
        print("ERRO: Essa opção não está disponível...")
        continue

    elif opcao == 1: # CADASTRO DE NOVO ATIVO
        print("")
        print("=-=-=-=-=- CADASTRO DE NOVO ATIVO -=-=-=-=-=-=")
        print("")
        if lista_ativos:
            novo_id = max(ativo["id"] for ativo in lista_ativos) + 1
        else:
            novo_id = 1

        dados_ativo_novo = { #CADASTRO DE NOVO ATIVO COM DICIONARIO
            "id": novo_id,
            "nome": pedir_input(mensagem="Digite o nome do ativo: "),
            "responsavel": pedir_input(mensagem="Digite o responsável pelo ativo: "),
            "setor": pedir_input(mensagem="Digite o setor responsável: "),
            "tipo": exibir_tipos_de_ativos() or pedir_tipo_de_ativo(),
            "vulnerabilidades": [],
        }
        print("")
        lista_ativos.append(dados_ativo_novo)

        if salvar_arquivos(lista_ativos):
            print("Ativo cadastrado com sucesso!")

    elif opcao == 2: # CADASTRO DE VULNERABILIDADES

        if lista_ativos == []:
            print("Não há ativos cadastrados!")
            continue
        else:
            print("")
            print("=-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-=")
            print("")
            for ativo in lista_ativos:
                print(f"ID:{ativo['id']} - {ativo['nome']}")
                print("")

            while True:
                escolha_id = verificar_int("Digite o ID do ativo selecionado: ")
                print("")
                encontrado = False
                for ativo in lista_ativos:
                    if ativo['id'] == escolha_id:
                        encontrado = True

                        nome = pedir_input(mensagem="Digite um nome para a vulnerabilidade: ")
                        descricao = pedir_input("Digite uma descrição: ")
                        categoria = pedir_input("Digite uma categoria: ")
                        severidade = pedir_severidade()
                        status = pedir_input("Status de tratamento: ")

                        vulne_nova = {'nome': nome,
                                      'descricao': descricao,
                                      'categoria': categoria,
                                      'severidade': severidade,
                                      'status': status}
                        
                        ativo['vulnerabilidades'].append(vulne_nova)

                        if salvar_arquivos(lista_ativos):
                            print("")
                            print("Vulnerabilidade cadastrada com sucesso!")
                        break
                    
                if encontrado:
                    break

                if not encontrado:
                      print("Esse ID não está cadastrado!")
                      continue     

    elif opcao == 3: # LISTAGEM DE ATIVOS CADASTRADOS
        print("")
        if lista_ativos == []:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("")
            print("Não há ativos cadastrados!")
            continue
        else:
            print("=-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-=")
            print("")
            for ativo in lista_ativos:
                print(f"ID:{ativo['id']} - {ativo['nome']}")

    elif opcao == 4: # BUSCA E CONSULTA DE ATIVOS
        print("""
=-=-=-=-=-=-=-=-=-= OPÇÕES =-=-=-=-=-=-=-=-=-=

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
                print("Esse ID não foi encontrado!")
                continue
            else:
                for ativo in lista_ativos:
                    if ativo["id"] == id_digitado:

                        print("-=-=-=-=-=-=- ATIVO ENCONTRADO -=-=-=-=-=-=-=-")
                        print("")
                        Exibe_Dados_ativo(ativo)
                        print("")

                        if len(ativo['vulnerabilidades']) == 0:
                            print("Nenhuma vulnerabilidade cadastrada.")
                        else:
                            Exibe_Vulnerabilidades_ativo(ativo)

        elif busca_opcao == 2: 
            nome_digitado = input("Digite o nome do ativo que deseja buscar: ").strip()
            print("")
            if nome_digitado.lower() not in (ativo['nome'].lower() for ativo in lista_ativos):
                print("Esse nome não pertence a um ativo cadastrado!")
                continue
            else:
                for ativo in lista_ativos:
                    if ativo["nome"].lower() == nome_digitado.lower():
                        # os lower() é só pra garantir que ambos textos estejam minusculos, ou seja, iguais
                        print("-=-=-=-=-=-=- ATIVO ENCONTRADO -=-=-=-=-=-=-=-")
                        print("")
                        Exibe_Dados_ativo(ativo)

                        print("")
                        if len(ativo['vulnerabilidades']) == 0:
                            print("Nenhuma vulnerabilidade cadastrada.")
                        else:
                            Exibe_Vulnerabilidades_ativo(ativo)

        elif busca_opcao == 3:
            continue

    elif opcao == 5: # ATUALIZAR ATIVOS 
        
        if lista_ativos == []:
            print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                
Não há ativos cadastrados!""")

        else:
            print("""
=-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-=
            
Qual ativo você deseja atualizar?
                """)
            for ativo in lista_ativos:
                print(f"ID:{ativo['id']} - {ativo['nome']}")
                print("")
                

            while True:
                id_escolhido = verificar_int("Digite o ID do ativo que deseja atualizar: ")

                encontrado = False
                for ativo in lista_ativos:
                    if ativo['id'] == id_escolhido:
                        encontrado = True
                        while True:
                            print("""
-=-=-=-=-=- ATUALIZAÇÃO DE ATIVO -=-=-=-=-=-=-

O que deseja atualizar no ativo?

1 - Nome
2 - Responsável
3 - Setor
4 - Tipo
5 - Voltar ao menu principal
""")
                            
                            escolha_atualizar = verificar_int("Digite uma opção: ")
                            print("")

                            if escolha_atualizar not in range(1, 6):
                                print("Essa opção não está disponível!")
                                continue

                            elif escolha_atualizar == 1:
                                print(f"OBS: O nome atual é {ativo['nome']}")
                                ativo['nome'] = pedir_input(mensagem="Digite o novo nome do ativo: ")
                                if salvar_arquivos(lista_ativos):
                                    print("Nome alterado com sucesso!")
                                

                            elif escolha_atualizar == 2:
                                print(f"OBS: O responsável atual é {ativo['responsavel']}")
                                ativo['responsavel'] = pedir_input(mensagem="Digite o responsável pelo ativo: ")
                                if salvar_arquivos(lista_ativos):
                                    print("Responsável alterado com sucesso!")

                            elif escolha_atualizar == 3:
                                print(f"OBS: O setor responsável atual é {ativo['setor']}")
                                ativo['setor'] = pedir_input(mensagem="Digite o setor responsável: ")
                                if salvar_arquivos(lista_ativos):
                                    print("Setor alterado com sucesso!")

                            elif escolha_atualizar == 4:
                                print(f"OBS: O ativo atual é do tipo {ativo['tipo']}")
                                print("")
                                exibir_tipos_de_ativos()
                                ativo['tipo'] = pedir_tipo_de_ativo()
                                if salvar_arquivos(lista_ativos):
                                    print("Tipo do ativo alterado com sucesso!")

                            elif escolha_atualizar == 5:
                                break

                if encontrado:
                    break 

                if not encontrado:
                    print("Esse ID não está cadastrado!")

    elif opcao == 6: # REMOÇÃO DE ATIVOS
        if lista_ativos == []:
            print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    Não há ativos cadastrados!""")
            continue
        
        print("""
=-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-=

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
                    if salvar_arquivos(lista_ativos):
                        print("")
                        print("Ativo removido com sucesso!")
                    break

            if not encontrado:
                print("Esse ID não foi encontrado!")
                continue


            break

    elif opcao == 7: # SAIR DO PROGRAMA
        break
        