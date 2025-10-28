import doctest

def montaSequencia(n):
    """
    >>> montaSequencia(2)
    1 1 1
    1 2 2
    2 4 8
    2 5 9
    >>> montaSequencia(5)
    1 1 1
    1 2 2
    2 4 8
    2 5 9
    3 9 27
    3 10 28
    4 16 64
    4 17 65
    5 25 125
    5 26 126
    >>> montaSequencia(3)
    1 1 1
    1 2 2
    2 4 8
    2 5 9
    3 9 27
    3 10 28
    >>> montaSequencia(4)
    1 1 1
    1 2 2
    2 4 8
    2 5 9
    3 9 27
    3 10 28
    4 16 64
    4 17 65
    """
    for i in range(1,n+1):
        print(f'{i} {i**2} {i**3}')
        print(f'{i} {i**2+1} {i**3+1}')

def main():
    n = int(input())
    montaSequencia(n)
    doctest.testmod()
    
if __name__ == '__main__':
    main()