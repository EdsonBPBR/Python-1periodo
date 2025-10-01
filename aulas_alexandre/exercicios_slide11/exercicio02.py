lista = []

while True:
    numero = int(input())
    
    if numero == 0:
        break   
    
    lista.append(numero)
    
valor = int(input("Informe o número para buscar: "))
print(f'{valor} aparece {lista.count(valor)} vezes')
