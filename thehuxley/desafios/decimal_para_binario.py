# Dado um número n na base decimal, escreva uma função recursiva que converte este número para binário. 

def decimalparabinario(decimal, binario = []):
    c = decimal
    while True:
        binario.append(c % 2)
        c = c // 2
        if c == 0:
            break
        
    binario.reverse()
    for b in binario:
        print(b)

if __name__ == '__main__':
    n = int(input())
    decimalparabinario(n)