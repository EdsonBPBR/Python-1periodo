n = int(input())
numeros = []
entrada = str(input()).split()
for i in entrada:
    numeros.append(int(i))
    
def calcula_media(n):
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
        
k = [] # poderia usar um conjunto
for posicao in range(len(numeros)):
    if not(numeros[posicao] in k):
        if posicao == 0:
            maior = numeros.count(numeros[posicao])
            valor = numeros[posicao]
    
        else:
            if numeros.count(numeros[posicao]) > maior:
                maior = numeros.count(numeros[posicao])
                valor = numeros[posicao] # fiquei para terminar isso, ele está calculando a moda, no entantanto a quest~eos pode mais
                
         
                
print(f'Media: {calcula_media(n):.2f}')
print(f'Mediana: {calcula_mediana(numeros):.2f}')
