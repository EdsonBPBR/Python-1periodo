# 10 (Produt ́orio) Crie um programa em Python para receber 10 valores e informar o
# produt ́orio destes valores

produtorio = 1
for a in range(10):
    valor = float(input('Informe um valor: '))

    produtorio *= valor

print(f'O produto dos valores informados é {produtorio:.2f}')