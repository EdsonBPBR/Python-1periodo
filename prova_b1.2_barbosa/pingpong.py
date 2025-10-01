import doctest

def PingPong(n, m):
    for a in range(n, m+1):
        if a % 3 == 0:
            print('ping')

        elif a % 5 == 0:
            print('pong')
        
        elif (a % 3 == 0) and (a % 5 == 0):
            print('ping-pong')
            
        else:
            print(a)

if __name__ == '__main__':
    n = int(input('Entrada N: '))
    m = int(input('Entrada M: '))

    PingPong(n, m)
