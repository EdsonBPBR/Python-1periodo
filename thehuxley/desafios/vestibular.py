# A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão. A primeira linha da entrada contém um único inteiro N, indicando o número de questões da prova. A segunda linha da entrada contém uma cadeia de N caracteres, indicando o gabarito da prova. A terceira linha da entrada contém outra cadeia de N caracteres, indicando as opções marcadas pelo candidato. Ambas as cadeias contêm apenas os caracteres 'A', 'B', 'C', 'D' e 'E' (sempre em letra maiúscula). # 1 ≤ N ≤ 80

if __name__ == '__main__':
    tamanho_gab = int(input())

    entrada_gab = str(input())
    gab = list(entrada_gab)

    pont = 0

    entrada_gab_cand = str(input())
    gab_cand = list(entrada_gab_cand)

    for posicao in range(tamanho_gab):
        if gab[posicao] == gab_cand[posicao]:
            pont += 1
    print(pont)