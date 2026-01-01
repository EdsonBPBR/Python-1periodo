entrada = str(input()).split()

def verificaPrimo(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0 :
        return False
    c = 0
    for k in range(3, int(n**0.5) + 1, 2): 
        if n % k == 0:
            c = 1
            break
    if c > 0:
        return False
    else:
        return True

i = 0
for posicao, caractere in enumerate(entrada):
    if int(caractere) <= 0:
        break
    
    if verificaPrimo(int(caractere)):
        if i == 0:
            maior_primo = int(caractere)
        else:
            if int(caractere) > maior_primo:
                maior_primo = int(caractere)
    else:
        print(int(caractere))

print(maior_primo)