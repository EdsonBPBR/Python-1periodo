# Leia uma sequência de 101 números inteiros , verifique se o último número está presente nos 100 primeiros números e imprima as posições do array em que ele está presente.
lista = []
chaves = []

for a in range(100):
    n = int(input())
    lista.append(n)
    
m = int(input())

for a in range(len(lista)):
    if lista[a] == m:
        print(a)