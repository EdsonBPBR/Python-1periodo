def receber_entradas(n):
    pares = []
    impares = []
    for _ in range(n):
        entrada = str(input()).split()
        if int(entrada[1]) % 2 == 0:
            pares.append(entrada[0])
        else:
            impares.append(entrada[0])
        
    return pares, impares
    
def exibir_saida(pares, impares):
    for pessoas in pares:
        print(pessoas)
    for pessoas in impares:
        print(pessoas)
        
def main():
    try:
        n = int(input())
        pares, impares = receber_entradas(n)
        exibir_saida(pares, impares)
    except:
        pass
    
if __name__ == '__main__':
    main()