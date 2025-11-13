tamanho = int(input())
array = []
saida = []
for _ in range(tamanho):
    saida.append('-')
while True:
    opc = str(input()).split()
    if opc[0] == 'E':
        if len(array) >= tamanho:
            print('Fila cheia')
        else:  
            elemento = int(opc[1])
            array.append(elemento)
            for i in range(len(array)):
                saida[i] = array[i]    
                
            for indice, valor in enumerate(saida):
                if len(saida) - 1 == indice:
                    print(f'{valor}\n', end='')
                else:
                    print(f'{valor}', end=' ')
            
    elif opc[0] == 'D':
        if len(array) < 1:
            print('Fila vazia')
        else:
            array.remove(array[0])
            # FIQUEI PARA TERMINAR A SAIDA DESSA PORRA
            # saida[0] = '-'
            for posicao, valor in enumerate(saida):
                if array[0] == valor:
                    saida[posicao-1] = '-'
                    print(valor)
               
            for indice, valor in enumerate(saida):
                if len(saida) - 1 == indice:
                    print(f'{valor}\n', end='')
                else:
                    print(f'{valor}', end=' ')
            
    elif opc[0] == 'F':
        print('Saindo...')