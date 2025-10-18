# você deverá ler 15 valores colocá-los em 2 arrays conforme estes valores forem pares ou ímpares.
# Só que o tamanho de cada um dos dois arrays é de 5 posições
# Então, cada vez que um dos dois arrays encher, você deverá imprimir todo o array e utilizá-lo novamente para os próximos números que forem lidos. 
# Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois arrays, imprimindo primeiro os valores do array ímpar.
pares = []
impares = []

for _ in range(15):
    
    if len(pares) == 5:
        for indice, valor in enumerate(pares):
            print(f'par[{indice}] = {valor}')
        pares.clear()
    
    if len(impares) == 5:
        for indice, valor in enumerate(impares):
            print(f'impar[{indice}] = {valor}')
        
        impares.clear()
    
    n = int(input())
    
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
        
for indice, valor in enumerate(impares):
    print(f'impar[{indice}] = {valor}')

for indice, valor in enumerate(pares):
    print(f'par[{indice}] = {valor}')