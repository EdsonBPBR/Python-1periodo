def calcula_media(n, numeros):
    somatorio = 0
    for numero in numeros:
        somatorio += numero
    return somatorio/n

def calcula_mediana(numeros):
    numeros.sort()
    if len(numeros) % 2 == 1:
        mediana = numeros[(len(numeros)//2)]
    else:
        mediana = (numeros[(len(numeros)//2)] + numeros[(len(numeros)//2)-1])/2
    return mediana
      
def calcula_moda(numeros):    
    k = []
    maior = 0
    valor = 0
    tem_moda = True 
    for posicao in range(len(numeros)):
        if not(numeros[posicao] in k):
            freq_atual = numeros.count(numeros[posicao])
            
            if freq_atual > maior:
                maior = freq_atual
                valor = numeros[posicao]
                tem_moda = True 
            elif freq_atual == maior and numeros[posicao] != valor:
                tem_moda = False 
            
            k.append(numeros[posicao])
    return tem_moda, maior, valor

def exibir_moda(numeros):
    tem_moda, maior, valor = calcula_moda(numeros)
    if tem_moda and maior > 1:  
        return f'Moda: {valor:.2f}'
    else:
        return 'Nao tem moda'

def main():
    n = int(input())
    numeros = []
    entrada = str(input()).split()
    for i in entrada:
        numeros.append(int(i))
                    
    print(f'Media: {calcula_media(n, numeros):.2f}')
    print(f'Mediana: {calcula_mediana(numeros):.2f}')
    print(exibir_moda(numeros))

if __name__ == '__main__':
    main()