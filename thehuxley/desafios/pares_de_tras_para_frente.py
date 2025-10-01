print('Digite os 10 numeros inteiros:')
lista = []

for a in range(10):
    numero = int(input())
    lista.append(numero)

lista.reverse()

print('Numeros pares na ordem inversa:')
for posicoes in range(len(lista)):
    if lista[posicoes] % 2 == 0:
        print(lista[posicoes], end=' ')
    