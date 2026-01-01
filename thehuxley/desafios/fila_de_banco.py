n, m, k = map(int, input().split())
fila1 = []
fila2 = []
nova_fila = []
for _ in range(n): fila1.append(int(input()))
for _ in range(m): fila2.append(int(input()))

for i in range(len(fila1)):
    nova_fila.append(fila1[i])
    nova_fila.append(fila2[i])
    
if n > m: 
    maior = n
else:
    maior = m

for i in range((m+n)-len(nova_fila)):
    print(i)