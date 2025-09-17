# Uma pessoa aplicou seu capital a juros e deseja saber, trimestralmente, a posição de seu investimento C inicial. Chamando de i a taxa de juros do trimestre,
# escreva uma tabela que, para cada trimestre, dê o rendimento auferido e o saldo acumulado durante um período de X anos, supondo-se que nenhuma retirada tenha sido feita.
#juros compostos

def calculaJurosComposto(C, i, k):
    M = C * ((1 + i)**k)
    juros = ((C * ((1 + i)**k)) - C)

    return M, juros

def obtemDadosEntrada(entrada):
    C = float(entrada[0])
    i = float(entrada[1])
    t = int(entrada[2]) * 4 

    return C, i, t

if __name__ == '__main__':
    entrada = str(input()).split()
    C, i, t = obtemDadosEntrada(entrada)

    juros_anterior = 0
    for k in range(1,t+1):
        M, juros = calculaJurosComposto(C, i, k)

        rendimento = juros - juros_anterior
        juros_anterior = juros

        print(f'Rendimento: {rendimento:.2f} Montante: {M:.2f}')