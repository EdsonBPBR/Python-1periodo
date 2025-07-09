bebidas = []

for b in range(1,6):
    nome = input(f'Nome da {b}ª bebida: ')
    bebidas.append(nome)

for bebida in sorted(bebidas):
    print(bebida)
