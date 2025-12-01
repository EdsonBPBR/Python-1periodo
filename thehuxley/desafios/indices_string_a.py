caracteres = []
frase = str(input())
for caractere in frase:
    caracteres.append(caractere)
letra = str(input())
for caractere in caracteres:
    if caractere == letra:
        print(caracteres.index(caractere))
        caracteres[caracteres.index(caractere)] = 0
        
print(-1)