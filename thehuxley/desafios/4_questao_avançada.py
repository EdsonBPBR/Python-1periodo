def verificaPares(entrada):
    pares = []
    for elementos in entrada:
        if int(elementos) % 2 == 0:
            pares.append(int(elementos))
    return pares
            
if __name__ == '__main__':
    try:
        entrada = str(input("Digite números separados por espaço: ")).split()
        print(f'Lista de pares: {verificaPares(entrada)}')
    except ValueError:
        print('Dado de entrada inválido!')