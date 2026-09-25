Sistema de Inventário de Ativos
Sobre o projeto

Sistema de inventário de ativos de TI desenvolvido em Python. Ele permite cadastrar e consultar ativos, além de registrar as vulnerabilidades associadas a cada um.

Funcionalidades

Cadastrar, listar, buscar, atualizar e remover ativos.

Buscar ativos por ID ou nome.

Cadastrar vulnerabilidades em um ativo e consultá-las junto com seus dados.

Confirmar a remoção de um ativo após avisar que suas vulnerabilidades também serão excluídas.

Como executar

É necessário ter Python instalado. No terminal, entre na pasta do projeto e execute:

python main.py


O programa apresenta um menu no terminal. Digite o número da opção desejada e siga as instruções exibidas.

Como obter o projeto

O repositório é público, portanto não é necessário possuir uma conta no GitHub ou estar autenticado para clonar o projeto.

No terminal, execute:

git clone https://github.com/gustavoufu/sistema-inventario.git


Depois, entre na pasta do projeto:

cd sistema-inventario


Em seguida, execute o programa:

python main.py


Caso o comando python não esteja disponível, pode ser necessário utilizar:

python3 main.py

Dados armazenados

Os ativos são guardados no arquivo arquivoativos.json. Ao iniciar, o programa carrega esse arquivo para a lista lista_ativos. Após operações que alteram os dados, ele tenta salvar a lista atualizada no arquivo.

Cada ativo possui ID, nome, responsável, setor, tipo e uma lista de vulnerabilidades. Cada vulnerabilidade possui nome, descrição, categoria, severidade e status de tratamento.