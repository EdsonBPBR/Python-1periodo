# Leia um inteiro N.

# Depois, leia até 20 inteiros X0, X1, ..., X20. Seu programa deve imprimir quantas vezes o inteiro N aparece nos X inteiros.

n = int(input())
frequencia = 0

c = 0

while c < 20:
    c += 1
    numero = int(input())
    
    if numero == -1:
        break
    
    if numero == n:
        frequencia += 1

print(f'{n} apareceu {frequencia} vezes')