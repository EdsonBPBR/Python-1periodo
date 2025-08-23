# 5 (Maior de 10) Crie um programa em Python para receber 10 valores e determinar
# qual foi o maior valor dentre os n ́umeros fornecidos

maior = 0
for k in range(3):
    valor = int(input('Informe um valor: '))
    
    if valor > maior:
        maior = valor

print(maior)