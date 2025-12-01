def monta_matriz():
    matriz = []
    for i in range(5):
        linha = []
        entrada = str(input()).split()
        for caractere in entrada:
            linha.append(caractere)
        matriz.append(linha)
    return matriz

def calcula_tempo(matriz):
    registro = []
    y = 0
    for i in range(5):
        x = 0
        for j in range(10):
            if matriz[i][j] == '0':
                tempo = (((x**2 + y**2) ** (1/2)) * 20) + 40
                registro.append([tempo, y, x])
                
            elif matriz[i][j] == '1':
                tempo = (((x**2 + y**2) ** (1/2)) * 20)
                registro.append([tempo, y, x])
            x += 1
        y += 1
    registro.sort(key=lambda item: (item[0], item[1]))
    return registro

def main():
    registro = calcula_tempo(monta_matriz())
    if len(registro) > 0:
        print(f'Vai la pro computador {registro[0][2]} da fileira {registro[0][1]}')
    else:
        print('Tristemente voce vai ter que aturar os PCs do grad 4')
        
if __name__ == '__main__':
    main()