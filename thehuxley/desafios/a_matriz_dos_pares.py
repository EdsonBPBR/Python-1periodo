n, m = map(int, input().split())

matriz = []
pares = []

c = 0
while True:
    c += 1
    if len(pares) == n:
        break
    if c % 2 == 0:
        pares.append(c) 
print(pares)

# continuar aqui, amanhã
