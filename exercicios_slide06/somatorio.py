# (Somat ́orio) Crie um programa em Python para receber 10 valores e informar o
# somat ́orio destes valores

somatorio = 0

for x in range(10):
    numero = float(input('Informe um valor: '))

    somatorio += numero 

print(f'O somatório dos valores informados é {somatorio}')