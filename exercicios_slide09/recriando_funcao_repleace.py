# Seja fornecida uma string, realize a substitui ̧c ̃ao de um caractere por outro (tal
# como na ‘fun ̧c ̃ao’ replace(c1, c2) )

#como funciona afunção replace??
# texto = 'Universidade'
# b = texto.replace('i', 'I')
# print(b)

# caractere_substituir = 's'
# caractere_atualizado = 'SS'

texto = 'Edson Barros'

def meuReplace(caractere_substituir, caractere_atualizado):
    novo_texto = ''

    c = 0
    while c < len(texto):
        if texto[c] == caractere_substituir:
            novo_texto += f'{caractere_atualizado}'
        else:
            novo_texto += texto[c]
        c += 1
    return novo_texto

if __name__ == '__main__':
    print(meuReplace('r', 'RRR'))