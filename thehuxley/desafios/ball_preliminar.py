lista = [2,2,3,2,2,2,3,2,2,2,2]
posicao, valor = map(int, input().split())
# print(lista[posicao-1])

while True:
    if lista[posicao-1] == valor:
        print(lista)
        lista.pop(posicao-1)
        print(lista)
        print(lista[posicao-1])
    input()
    print(lista)

# n = 1
# if lista[posicao-(n+1)] == lista[posicao-1]:
#     print(lista[posicao-(n+1)])
#     print('Sim')
# else:
#     print('Não')
    
# k = 0
# if lista[posicao+k] == lista[posicao-1]:
#     print(lista[posicao-(n+1)])
#     print('Sim')
# else:
#     print('Não')
    