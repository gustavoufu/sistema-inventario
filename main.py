from enum import Enum

class Status_dos_Ativos(Enum):
    ATIVO = "ativo"
    INATIVO = "inativo"
    MANUTENCAO = "manutenção"

nome = input("Digite o nome do ativo: ")
status_entrada = input("Digite o status do ativo: ")

status = Status_dos_Ativos(status_entrada)

print("-=-=-=-=-=Informações-=-=-=-=-=-")
print(f"Nome do ativo: {nome}")
print(f"Status:", status.value)

if status == Status_dos_Ativos.ATIVO:
    print("Situação: O ativo está funcionando!")
elif status == Status_dos_Ativos.INATIVO:
    print("Situação: O ativo está inativo!")
elif status == Status_dos_Ativos.MANUTENCAO:
    print("Situação: O ativo está em manutenção")