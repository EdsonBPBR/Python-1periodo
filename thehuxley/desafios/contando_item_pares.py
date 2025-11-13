def nParesMatriz(l,c):
    n_pares = 0
    for i in range(l):
        for j in range(c):
            elemento = int(input())
            if elemento % 2 == 0:
                n_pares += 1
    return n_pares

def main():
    l = int(input())
    c = int(input())
    print(nParesMatriz(l, c))

if __name__ == '__main__':
    main()