x = int(input('base: '))
n = int(input('expoente: '))

def potenciacao(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n > 1:
        return potenciacao(x, n-1) * x
    
print(potenciacao(x,n))
