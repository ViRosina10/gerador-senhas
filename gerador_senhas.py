import random
import string

def gerar_senha_simples(tamanho=8):
    """Gera uma senha simples com letras maiúsculas e minúsculas."""
    caracteres = string.ascii_letters
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    print("Senha gerada:", gerar_senha_simples(tamanho))
"Adiciona funcionalidade de geração de senhas simples".
