lista = []

while True:
    numero = int(input())
    
    if numero == 0:
        break   
    
    lista.append(numero)
    
print(f'Maior valor informado: {max(lista)}')
print(f'Soma dos valores informados: {sum(lista)}')