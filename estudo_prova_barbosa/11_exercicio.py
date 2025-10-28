def pell(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return 2*pell(n-1) + pell(n-2)
    
x = int(input())
print(pell(x))
