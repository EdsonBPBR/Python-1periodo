# Escrever um algoritmo que lê 5 valores para "a", um de cada vez, e conta quantos destes são negativos, escrevendo esta informação.

c = 0
negativos = 0

while c < 5:
    numero = float(input())  
    if numero < 0:
        negativos += 1
    c += 1

print(f'Foram digitados {negativos} numeros negativos')