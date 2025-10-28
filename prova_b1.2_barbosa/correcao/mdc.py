import doctest
def mdc(n, m):
    """
    >>> mdc(12,18)
    6
    >>> mdc(5,1)
    1
    >>> mdc(7560,19800)
    360
    >>> mdc(0,1)
    1
    """
    
    if n > m:
        maior = n
    else:
        maior = m

    for i in range(1,maior+1):
        if i == 1:
            maior_divisor = i
        else:
            if n % i == 0 and m % i == 0:
                maior_divisor = i
                
    return maior_divisor

def main():
    n = int(input())
    m = int(input())
    print(mdc(n, m))
    doctest.testmod()
    
if __name__ == '__main__':
    main()