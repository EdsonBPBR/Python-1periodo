lista = []

while True:
    numero = int(input())
    
    if numero == 0:
        break   
    
    lista.append(numero)
    
valor = int(input("Informe o número para buscar: "))

contador = 0
for elemento in lista:
    if elemento == valor:
        contador += 1

print(f'O valor informado {valor} aparece {contador} vezes')