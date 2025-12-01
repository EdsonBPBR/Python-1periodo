def inserir_numeros(lista, divisiveis):
    for _ in range(10):
        try:
            numero = int(input())
            if numero % 3 == 0:
                divisiveis.append(numero)
            lista.append(numero)
        except ValueError:
            print('Dado de entrada inválido!')

def main():
    lista = []
    divisiveis = []
    inserir_numeros(lista, divisiveis)
    print(f'Média: {sum(lista)/10}')
    print(f'Divisíveis: {sum(divisiveis)}')

if __name__ == '__main__':
    main()