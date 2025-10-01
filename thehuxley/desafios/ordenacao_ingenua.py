# Dado um conjunto de n valores inteiros, ordene-os em ordem crescente.
n = int(input())
lista_total = []

for _ in range(n):
    lista_elemento = []
    numero = int(input())
    lista_elemento.append(numero)
    lista_total.append(lista_elemento)
    
lista_total.sort()

for index in range(len(lista_total)):
    print(lista_total[index], end='')
    