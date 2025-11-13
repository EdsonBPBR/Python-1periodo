l, c = map(int, input().split())
matriz = []
menores_que_zero = 0
maiores_que_zero = 0
somatorio_diagonal_primaria = 0
somatorio_diagonal_secundaria = 0

# montar matriz
for i in range(l):
    linha = []
    for j in range(c):
        elemento = int(input())
        if elemento > 0:
            maiores_que_zero += 1
        else:
            menores_que_zero += 1
        
        linha.append(elemento)
    matriz.append(linha)

print('Matriz formada:')
# imprimir matriz:
for i in range(l):
    linha = ''
    for j in range(c):     
        if i == j:
            somatorio_diagonal_primaria += matriz[i][j]   
        linha += f'{matriz[i][j]} '
    print(linha.strip())

# diagonal secundaria:
if l == c:
    o = 0
    for i in range(l-1,-1,-1):
        somatorio_diagonal_secundaria += matriz[o][i]
        o += 1
        
    print(f'A diagonal principal e secundaria tem valor(es) {somatorio_diagonal_primaria} e {somatorio_diagonal_secundaria} respectivamente.')
else:
    print('A diagonal principal e secundaria nao pode ser obtida.')
print(f'A matriz possui {menores_que_zero} numero(s) menor(es) que zero.')
print(f'A matriz possui {maiores_que_zero} numero(s) maior(es) que zero.')