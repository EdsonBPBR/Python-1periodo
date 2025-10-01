import doctest

def calculaMDC(numero1, numero2):
    """
    Informar o maior divisor comum dentre dois números inteiros positivos e não nulos
    
    >>> calculaMDC(6,12)
    6
    >>> calculaMDC(12,18)
    6
    >>> calculaMDC(5,15)
    5
    >>> calculaMDC(5,10)
    5
    """

    if numero1 > numero2:
        maior = numero1
    elif numero1 == numero2 :
        maior = numero1
    else:
        maior = numero2


    for a in range(1, maior+1):
        if numero1 % a == 0 and numero2 % a == 0:
            if a == 1:
                mdc = a
            else:
                if a > mdc:
                    mdc = a
    return mdc

if __name__ == '__main__':
    numero1 = int(input())
    numero2 = int(input())

    doctest.testmod()
    print(calculaMDC(numero1, numero2))
