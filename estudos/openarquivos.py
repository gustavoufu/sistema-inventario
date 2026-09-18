import json

lista_ativos = []

while True:

    temp_ativo = {"nome": input("Digite o nome para o ativo: "),
                  "setor": input("Digite o setor do ativo: "),
                  "vulnerabilidade": input("Digite a vulnerabilidade do ativo")}
    lista_ativos.append(temp_ativo)
    break


with open("estudos/Vulnerabilidades.json", "w") as vulne:
    json.dump(lista_ativos, vulne)

with open("estudos/Vulnerabilidades.json", "r") as vulne:
    lido = json.load(vulne)

for pessoa in lido:
    for k, v in pessoa.items():
        print(f"A key é {k} e o valor é {v}...")