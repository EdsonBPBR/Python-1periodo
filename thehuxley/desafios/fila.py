
if __name__ == '__main__':
    fila = []

    while True:
        try:
            entrada = str(input()).split()
            opcao = entrada[0]
            elemento = entrada[1]
            
            if opcao == 'Finalizar':
                break
            
            elif opcao == 'Enfileirar':
                fila.append(elemento)
                
        except IndexError:
            if opcao == 'Imprimir':
                for posicoes in range(len(fila)):
                    
                    if posicoes == len(fila)-1:
                        print(f'{fila[posicoes]}', end='')
                    else:
                        print(f'{fila[posicoes]}', end=' ')
                    
                print()
            
            elif opcao == 'Finalizar':
                break
            
            elif opcao == 'Desenfileirar':
                if len(fila) > 0:
                    fila.pop(0)