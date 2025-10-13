# Dado um array de números inteiros, seu trabalho deve ser encontrar quais elementos do array original continuam na mesma posição depois que o array for ordenado e qual é sua posição.

# 2 2 3 1 2 3
# 3 2 1 3 2 2

n = int(input())
entrada = str(input()).split()
array_original = []

for caractere in entrada:
    array_original.append(int(caractere))
    
array_ordenado = list(array_original)
array_ordenado.sort()

c = 0
for i in range(n): # contador
    if array_original[i] == array_ordenado[i]:
        c += 1

print(c) 

ocorrencias = []
for i in range(n): 
    if array_original[i] == array_ordenado[i]:
        ocorrencias.append(array_ordenado[i], ) # eu parei aqui, o B.O está aqui vum
        
print(ocorrencias)