def calculaProdutorioDiagonal(n):
    elementos_diagonal = []
    
    for i in range(n):
        for j in range(n):
            elemento = int(input())  
            if i == j:
                elementos_diagonal.append(elemento)

    produtorio = 1
    for numero in elementos_diagonal:
        produtorio *= numero

    return produtorio   

def main():
    n = int(input())
    print(f'{calculaProdutorioDiagonal(n):.1f}')

if __name__ == '__main__':
    main()