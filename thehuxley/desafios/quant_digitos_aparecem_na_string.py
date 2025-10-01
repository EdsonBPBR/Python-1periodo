c = 0
texto = str(input())
digitos = '0123456789'

for a in range(len(texto)):
    if texto[a] in digitos:
        c += 1

print(c)