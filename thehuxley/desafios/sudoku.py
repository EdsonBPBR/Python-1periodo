# fragmento_matriz = []
# valido = True

# for i in range(3):
#     for k in range(3):
#         elemento = int(input())
#         fragmento_matriz.append(elemento)
    
# for i in range(1, 10):
#     if not (i in fragmento_matriz):
#         valido = False
#         break

valido = True

sla = {
    0: [],
    1: [],
    2: []
}

for _ in range(3):
    linha = str(input()).split()
    k = 0
    c = 3
    
    for i in range(3):
        for j in linha[k:c]:
            sla[i].append(int(j))
            sla[i].sort()
        k = c
        c += 3
        
    print(sla)


# for p in sla.values():
#     fragmento_matriz = p
    
#     for i in range(1, 10):
#         print(i in fragmento_matriz)
#         if (i in fragmento_matriz):
#             continue
#         else:
#             valido = False
#             break