lista = []

while True:
    numero = int(input())    
    if numero == 0:
        break   
    
    lista.append(numero)

somatorio = 0
for index in range(len(lista)):
    if index == 0:
        maior = lista[index]
    else:
        if lista[index] > maior:
            maior = lista[index]
            
    somatorio += lista[index]
    
print(f'O maior número informado foi: {maior}')   
print(f'Soma dos valores informados: {somatorio}')