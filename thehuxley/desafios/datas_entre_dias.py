# Dado um array de números inteiros, seu trabalho deve ser encontrar quais elementos do array original continuam na mesma posição depois que o array for ordenado e qual é sua posição.

tamanho = int(input())
entrada = str(input()).split()
lista_elementos = []
lista_ordenada = []

for elementos in entrada:
    lista_elementos.append(int(elementos))

lista_elementos.sort()

for k in lista_elementos:
    lista_ordenada.append(k)

n_semelhanca = 0 
a = 0

while a < 6:
    if entrada[a] == str(lista_ordenada[a]):
        n_semelhanca += 1
    a += 1

print(n_semelhanca)

k = 0
while k < 6:
    if entrada[k] == str(lista_ordenada[k]):
        print(f'{entrada[k]} {k+1}')
    k += 1
