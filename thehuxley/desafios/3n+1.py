# Por exemplo, a seguinte sequência de números será gerada quando n é 22: # 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# "tamanho do ciclo" de n é a quantidade de números gerados até o 1 (incluindo o próprio 1). No exemplo acima, o "tamanho do ciclo" de 22 é 16. 

# o que eu criei:
# while True:
#     try:
#         dados = str(input()).strip().split()
#         if not dados:
#             break
    
#         i = int(dados[0])
#         j = int(dados[1])
        
#         inicio = min(i, j)
#         fim = max(i, j)
        
#         for a in range(inicio, fim + 1):                
#             ciclo = []
#             x = a
#             while True:
#                 ciclo.append(int(x))
#                 if x == 1:
#                     break
                
#                 if x % 2 == 0:
#                     x = x / 2
#                 else:
#                     x = (3 * x) + 1
            
#             if a == inicio: 
#                 maior = len(ciclo)
#             else:
#                 if len(ciclo) > maior:
#                     maior = len(ciclo)

#         print(f'{i} {j} {maior}')
#     except EOFError:
#         break

# gerado por IA para melhorar a eficiência: 
# Cache global para armazenar tamanhos de ciclo já calculados
cache = {}

def calcular_ciclo(n):
    if n in cache:
        return cache[n]
    
    original = n
    comprimento = 1  # Começa com o próprio n
    
    while n != 1:
        if n in cache:
            comprimento += cache[n] - 1
            break
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        comprimento += 1
    
    cache[original] = comprimento
    return comprimento

while True:
    try:
        dados = input().strip().split()
        if not dados:
            break
    
        i = int(dados[0])
        j = int(dados[1])
        
        inicio = min(i, j)
        fim = max(i, j)
        
        maior = 0
        for a in range(inicio, fim + 1):
            comprimento = calcular_ciclo(a)
            if comprimento > maior:
                maior = comprimento

        print(f'{i} {j} {maior}')
    except EOFError:
        break