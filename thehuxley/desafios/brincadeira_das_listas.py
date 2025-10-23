lista_original = []
x = lista_original
lista_invertida = []
lista_elementos_pares_impares = []
lista_resultante = []

entrada = str(input()).split()
for caracteres in entrada:
    lista_original.append(int(caracteres))
    
x.reverse()
lista_invertida = x

for posicao in range(len(lista_original)-1, -1, -1):
    if posicao % 2 != 0:
        lista_elementos_pares_impares.append(lista_original[posicao])

for posicao in range(len(lista_original)-1, -1, -1):
    if posicao % 2 == 0:
        lista_elementos_pares_impares.append(lista_original[posicao])

for i in range(len(lista_invertida)):
    soma = lista_invertida[i] + lista_elementos_pares_impares[i]
    lista_resultante.append(soma)
    
invertidos = ''
for i in range(len(lista_invertida)):
    if len(lista_elementos_pares_impares) - 1 == i:
        invertidos += f'{lista_invertida[i]}'
    else:
        invertidos += f'{lista_invertida[i]} '
print(f'Invert: {invertidos}')

pares_impares = ''
for i in range(len(lista_elementos_pares_impares)):
    if len(lista_elementos_pares_impares) - 1 == i:
        pares_impares += f'{lista_elementos_pares_impares[i]}'
    else:
        pares_impares += f'{lista_elementos_pares_impares[i]} '
    
print(f'ParImp: {pares_impares}')

resul = ''
for i in range(len(lista_resultante)):
    resul += f'{lista_resultante[i]} '
    
print(f'Soma: {resul}')