def cadastrar_registros(t):
    registros = []
    for _ in range(t):
        entrada = str(input()).split()
        registros.append([entrada[0], int(entrada[1])])
    return registros

def verifica_idades(registros, idade):
    nomes = []
    for i in registros:
        if i[1] == idade:
            nomes.append(i[0])
    return nomes

def exibir_idades(nomes):
    if len(nomes) > 0:
        for posicao in range(len(nomes)):
            if len(nomes) - 1 == posicao:
                print(nomes[posicao], end='')
            else:
                print(nomes[posicao], end=' ')
    else:
        print(f'Eleven nao tem amigos com essa idade.')
        
def main():
    t = int(input())
    registros = cadastrar_registros(t)
    idade = int(input())
    exibir_idades(verifica_idades(registros, idade))
    
if __name__ == '__main__':
    main()