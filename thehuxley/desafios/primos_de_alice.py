# Alice é uma menina com vários probleminhas, dentre eles está o sei fascínio por números primos. Enquanto estava passeando no uninho de Aline, ela viu várias matrizes quadradas (não me pergunte como), sua tarefa vai ser pegar todos os primos em determinada matriz e ordena-los em forma crescente.
# Entrada: número n, que representará o número de linhas e colunas da matriz e os números da matriz
def verificaPrimo(n):
    if n <= 1:
        status = False
        return status
    
    if n == 2:
        status = True
        return status
    
    if n % 2 == 0:
        status = False
        return status
    
    c = 0
    for k in range(3, int(n**0.5) + 1, 2): 
        if n % k == 0:
            c = 1
            break
    
    if c > 0:
        status = False
        return status
    else:
        status = True
        return status
    
n = int(input())
primos = []

for a in range(n):
    dado_linha = str(input()).split()
    
    for posicoes in range(len(dado_linha)):
        if verificaPrimo(int(dado_linha[posicoes])):
            primos.append(int(dado_linha[posicoes]))
   
primos.sort()         

for elementos in primos:
    print(elementos, end=' ')