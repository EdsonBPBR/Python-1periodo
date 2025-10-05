# Leia 10 números inteiros.
# Depois leia mais um número inteiro x.
# Sua missão é imprimir quantas vezes x apareceu entre os 10 primeiros inteiros lidos.
numeros = []

for a in range(10):
    n = int(input())
    numeros.append(n)

m = int(input())
print(numeros.count(m))