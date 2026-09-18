import json

def verificar_int(mensagem): #VERIFICAR INT É LIGADO A UMA MENSAGEM INPUT
    while True:
        try:
            inteiro = int(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO, digite um número inteiro válido...")
            continue
        else: 
            return inteiro



try: 
    with open("arquivoativos.json", "r", encoding="utf-8") as arquivolista:
        lista_ativos = json.load(arquivolista)
except (FileNotFoundError, json.JSONDecodeError):
     lista_ativos = []



while True: #EXIBE AS OPCOES DO CRUD
    opcao = verificar_int("""
    -=-=-=-=-= OPÇÕES DE ATIVO =-=-=-=-=-=-

    1 - Cadastro de ativos
    2 - Listar ativos
    3 - Remover ativos
    4 - Sair

    Escolha uma opção: """)

    if opcao not in range(1, 5): #AVISA ERRO -> SE COLOCAR OPCAO QUE NAO EXISTE
        print("")
        print("ERRO: Essa opção não está disponível...")
        continue

    elif opcao == 1: #COLETA DADOS DO NOVO ATIVO PARA SUBIR NA LISTA DE DICIONARIOS
        print("")
        dados_ativo_novo = {"nome": input("Digite um nome para o ativo: "),
                            "setor": input("Digite o setor responsável: "),
                            "vulnerabilidade": input("Digite a vulnerabilidade: "),
                            "severidade": input("Digite um nível de severidade [1 até 5]: ")}
        lista_ativos.append(dados_ativo_novo)
        try: #ARMAZENA A NOVA MODIFICACAO NO ARQUIVO COM A LISTA DE ATIVOS
             with open("arquivoativos.json", "w", encoding="utf-8") as arquivolista:
                  json.dump(lista_ativos, arquivolista)
        except OSError: print("Não foi possível salvar os dados no arquivo.")


    elif opcao == 2: #LISTA TODOS OS DICIONARIOS NA LISTA "LISTA_ATIVOS"
        print("-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-")
        print("")
        for posicao, ativo in enumerate(lista_ativos, start=1):
            print(f"{posicao} - {ativo['nome']}")


    elif opcao == 3: #EXIBE A LISTA DE ATIVOS CADASTRADOS PARA ESCOLHA DE REMOCAO DE ATIVO
        print("-=-=-=-=-=- ATIVOS CADASTRADOS -=-=-=-=-=-=-")
        print("")
        print("Qual ativo você deseja remover?")
        print("")
        for posicao, ativo in enumerate(lista_ativos, start=1):
                    print(f"{posicao} - {ativo['nome']}")
        print("")

        while True: #CRIA UM LOOP PARA SELECIONAR UMA POSICAO DE ATIVO VALIDA PARA EXCLUIR
            escolha_rem = verificar_int("Escolha um ativo: ")
            if 1 <= escolha_rem <= len(lista_ativos):
                del lista_ativos[escolha_rem - 1]
                try: #ARMAZENA A NOVA MODIFICACAO NO ARQUIVO COM A LISTA DE ATIVOS
                     with open("arquivoativos.json", "w", encoding="utf-8") as arquivolista:
                            json.dump(lista_ativos, arquivolista)
                except OSError: print("Não foi possível salvar os dados no arquivo.")
                break
            else: 
                 print("Essa opção não está disponível")
                 continue
    elif opcao == 4:
         break