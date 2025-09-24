def verificaPrimo(n):
    c = 0
    
    if n == 0 or n == 1:
        print(0)
        
    else:
        if n > 2:
            if n % 2 == 0:
                c = 1
            else:
                for k in range(3, n):
                    if n % k == 0:
                        c += 1
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