n = int(input())
registros = []
dicionario = {}
for i in range(n):
    entrada = str(input()).strip().split()
    nota = int(entrada[0])
    preco = float(entrada[1])
    registros.append([nota, preco])

registros.sort()
for dado in registros:
    if not(dado[0] in dicionario):
        dicionario[dado[0]] = [dado[1]]
    else:
        dicionario[dado[0]].append(dado[1]) 
        dicionario[dado[0]].sort()
    
# print(dicionario)
chaves = list(dicionario.keys())

for chave in chaves[::-1]:
    # print(len(dicionario[chave]))
    # print(dicionario[chave])
    for i in range(len(dicionario[chave])):
        print(f'Nota: {chave}')
        print(f'Preco: {dicionario[chave][i]:.2f}\n')