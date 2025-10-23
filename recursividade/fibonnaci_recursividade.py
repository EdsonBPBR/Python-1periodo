# função de fibonacii em recursividade
def fibbonacci(n):
    if n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    elif n > 2:
        return (fibbonacci(n-1) + fibbonacci(n-2))
    
m = int(input())
for i in range(m):
    print(fibbonacci(i), end=' ')