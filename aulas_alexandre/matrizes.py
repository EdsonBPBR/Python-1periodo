def leitura_matriz():
    pass

def imprime_matriz():
    pass

def soma_matriz():
    pass

# quantidade de linhas: 2
# quantidade de colunas: 2

# a(0,0): 2
# a(0,1): 1
# a(1,0): 0
# a(1,1): 5

quant_linhas = int(input('Informe a quantidade de linhas: '))
quant_colunas = int(input('Informe a quantidade de colunas: '))

matriz = {
}

for a in range(quant_linhas):
    for b in range(quant_colunas):
        elemento = int(input(f"({a+1}, {b+1}) = "))
        matriz[(a, b)] = elemento

print(f'| {matriz[(0,0)]} {matriz[(0,1)]} |')
print(f'| {matriz[(1,0)]} {matriz[(1,1)]} |')