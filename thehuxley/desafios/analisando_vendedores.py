def buscar_melhor_pior(registros):
    registros.sort()    
    print(f'Melhor vendedor: {registros[-1][1]}')
    print(f'Vendas: R$ {registros[-1][0]:.2f}')
    print(f'Unidade: {registros[-1][2]}')
    print(f'Gerente: {registros[-1][3]}')
    print()
    print(f'Pior vendedor: {registros[0][1]}')    
    print(f'Vendas: R$ {registros[0][0]:.2f}')
    print(f'Unidade: {registros[0][2]}')
    print(f'Gerente: {registros[0][3]}')
    print()
    
def buscar_vendedor(nome, registros):
    cadastrado = False
    for posicao, registro in enumerate(registros):
        if registro[1] == nome:
            cadastrado = True
            index = posicao
            break
        
    if cadastrado:
        print(f'Nome: {registros[index][1]}')
        print(f'Vendas: R$ {registros[index][0]:.2f}')
        print(f'Unidade: {registros[index][2]}')
        print(f'Gerente: {registros[index][3]}')
        print()
    else:
        print('NAO ENCONTRADO')
        print()
        
def main():
    registros = []
    n = int(input())
    for _ in range(n):
        nome = str(input()).strip()
        vendas = float(input())
        unidade = int(input())
        gerente = str(input()).strip()
        registros.append((vendas, nome, unidade, gerente)) 

    buscar_melhor_pior(registros)
    while True:
        entrada = str(input()).strip()
        if entrada.upper() == 'OK':
            break
        
        buscar_vendedor(entrada, registros)

if __name__ == '__main__':
    main()