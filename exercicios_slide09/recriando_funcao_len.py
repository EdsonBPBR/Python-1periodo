# Seja fornecida uma string, informe quantos caracteres existem e qual  ́e o tamanho
# da string (tal como na fun ̧c ̃ao len(str) )

def meuLen(texto):
    tamanho = 0
    for _ in texto:
        tamanho += 1

    return (tamanho)

if __name__ == '__main__':
    print(meuLen('Ponciúncula'))


