# Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:
#     Primeiro os Pares;
#     Depois os Ímpares.
# Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

n = int(input())
pares = []
impares = []

for _ in range(n):
    m = int(input())
    if m % 2 == 0:
        pares.append(m)
    else:
        impares.append(m)

pares.sort()
impares.sort(reverse=True)

c = pares + impares
for elementos in c:
    print(elementos)