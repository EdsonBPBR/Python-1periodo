def verificaPrimo(n):
    if n <= 1:
        print(0)
        return
    
    if n == 2:
        print(1)
        return
    
    if n % 2 == 0:
        print(0)
        return
    
    c = 0
    for k in range(3, int(n**0.5) + 1, 2): 
        if n % k == 0:
            c = 1
            break
    
    if c > 0:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    while True:
        n = int(input())
        if n == -1:
            break
        verificaPrimo(n)
