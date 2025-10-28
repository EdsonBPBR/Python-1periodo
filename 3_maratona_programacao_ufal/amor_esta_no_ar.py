# 2 4 5 1 3
# 1 2 3 4 5

# 2 gosta 4
# 4 gosta 1
# 5 gosta 3
# 1 gosta 2
# 3 gosta 5
registros = {}
lista = [2, 4, 5, 1, 3]
for elemento in lista:
    print(f'{elemento} gosta de {lista[elemento-1]}')
    registros[elemento] = lista[elemento-1]
print(registros)

# verificação, núcleo principal da questão
c = 0
for chave in registros.keys():
    if c == 0:
        print(chave)
    else:
        print(chave)
    c += 1
    