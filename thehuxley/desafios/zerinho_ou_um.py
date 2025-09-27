# # O ganhador é aquele que tiver escolhido um valor diferente de todos os outros; se não há um jogador com valor diferente de todos os outros (por exemplo todos os jogadores escolhem zero, ou um grupo de jogadores escolhe zero e outro grupo escolhe um), não há ganhador.
# A entrada é composta por três inteiros A, B e C (A,B,C só podem ser 0 ou 1), indicando respectivamente os valores escolhidos por Alice, Beto e Clara.
def resultadoJogada(A, B, C):
    if (A == 1 and B == C == 0) or (A == 0 and B == C == 1):
        return ('A')

    elif (B == 1 and A == C == 0) or (B == 0 and A == C == 1):
        return ('B')

    elif (C == 1 and A == B == 0) or (C == 0 and A == B == 1):
        return ('C')

    else:
        return ('*')

if __name__ == '__main__':
    dados = str(input()).split()

    A = int(dados[0])
    B = int(dados[1])
    C = int(dados[2])

    print(resultadoJogada(A, B, C))
