def verificar_int(mensagem):
    while True:
        try:
            inteiro = int(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO, digite um número inteiro válido: ")
            continue
        else: return inteiro

digitado = verificar_int("Digite um número inteiro: ")
print(f"O número digitado foi {digitado}")