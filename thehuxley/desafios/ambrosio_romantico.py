# Por isso, Ambrósio analisou todas suas idéias e as classificou em uma escala de extravagância. Sabendo a quantidade perfeita para deixar sua namorada feliz, ele precisa agora verificar se existem duas opções entre suas idéias, que SOMADAS, combinem na extravagância perfeita
# Dois inteiros N (1 <= N <= 1000) e E (1 <= E <= 1000), representando o número de idéias, e a extravagância perfeita, respectivamente.

def pode_deixar_feliz(gestos, extr):
    vistos = set()
    for g in gestos:
        alvo = extr - g
        if alvo in vistos:
            return True
        vistos.add(g)
    return False


if __name__ == '__main__':
    n, extr = map(int, input().split())
    gestos = list(map(int, input().split()))

    if pode_deixar_feliz(gestos, extr):
        print("SIM")
    else:
        print("NAO")


