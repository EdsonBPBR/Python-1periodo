# A árvore de Natal é uma das mais populares tradições associadas com a celebração do Natal. É normalmente uma árvore conífera de folhas perenes (um pinheiro) ou uma árvore artificial. Jovander é professor de matemática e tem tido dificuldades em ensinar seus alunos como desenhar um triângulo isósceles. Para resolver tal problema, o professor pensou em construir um programa que desenhasse uma árvore de natal, em diferentes tamanhos, assim exemplificando o triângulo isósceles. No entanto, Jovander não tem afinidade com programação e pediu sua ajuda para construir este programa.
def montarArvore(n):
    caule = n // 2
    c = 1
    k = 0

    while c <= n:

        if k < n*2:
            k += 2
        else:
            break  
        print(f"{'X' * k:^{n*2}}".rstrip())
        
        c += 1

    c = 0
    while c < caule:
        print(f"{'XX':^{n*2}}".rstrip())

        c += 1

if __name__ == '__main__':
    n = int(input())
    montarArvore(n)
