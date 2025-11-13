tamanho = int(input())
sequencia = []
entrada_sequencia = str(input()).split()
for caracteres in entrada_sequencia:
    sequencia.append(int(caracteres))
    
tiros = int(input())
for _ in range(tiros):
    posicao, valor = map(int, input().split())
    print(sequencia[posicao-1])
    
    if sequencia[posicao-1] == valor:
        print('sim')
        # para frente
        