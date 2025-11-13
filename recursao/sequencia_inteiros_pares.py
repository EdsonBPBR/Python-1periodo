n = int(input())
# porque a desgraça da recursividade não exibe os outros valores? Não sei
def descrescente(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n
    else:
        return descrescente(n-1)

print(descrescente(n))