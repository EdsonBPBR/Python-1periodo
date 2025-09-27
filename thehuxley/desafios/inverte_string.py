# Leia uma string e inverta o seu conteúdo. Exemplo: Se a string digitada for "JANELA", então você deve imprimir: "ALENAJ".
def inversor(texto):
    return texto[::-1]

if __name__ == '__main__':
    texto = str(input())
    print(inversor(texto))
