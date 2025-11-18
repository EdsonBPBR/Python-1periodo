def calculoDistancia(x1,x2,y1,y2):
    distancia = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
    return distancia

def main():
    linha1 = str(input()).split()
    x1 = float(linha1[0])
    y1 = float(linha1[1])

    linha2 = str(input()).split()
    x2 = float(linha2[0])
    y2 = float(linha2[1])
    
    print(f'{calculoDistancia(x1,x2,y1,y2):.4f}')
    
if __name__ == '__main__':
    main()
    
    