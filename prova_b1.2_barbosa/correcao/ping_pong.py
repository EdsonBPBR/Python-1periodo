import doctest

def pingPong(n, m):
    """
    >>> pingPong(1,5)
    1
    2
    ping
    4
    pong
    >>> pingPong(2,9)
    2
    ping
    4
    pong
    ping
    7
    8
    ping
    >>> pingPong(5,30)
    pong
    ping
    7
    8
    ping
    pong
    11
    ping
    13
    14
    ping-pong
    16
    17
    ping
    19
    pong
    ping
    22
    23
    ping
    pong
    26
    ping
    28
    29
    ping-pong
    """
    for i in range(n, m+1):
        if (i % 3 == 0) and (i % 5 == 0):
            print('ping-pong')
            
        elif i % 3 == 0:
            print('ping')
            
        elif i % 5 == 0:
            print('pong')
            
        else:
            print(i)
            
def main():
    n = int(input())
    m = int(input())
    doctest.testmod()
    pingPong(n,m)
    
if __name__ == '__main__':
    main()