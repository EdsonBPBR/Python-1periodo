array = []
while True:
    opc = str(input()).split()
    if opc[0] == 'Empilhar':
        valor = int(opc[1])
        array.append(valor)
        
    elif opc[0] == 'Imprimir':
        for posicao, elemento in enumerate(array[::-1]):
            if len(array) -1 == posicao:
                print(f'{elemento}\n', end='')
            else:
                print(f'{elemento}', end=' ')
    
    elif opc[0] == 'Desempilhar':
        array.remove(array[::-1][0])
    
    elif opc[0] == 'Finalizar':
        break