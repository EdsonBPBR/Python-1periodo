import doctest

def soma(n1, n2):
    """
    >>> soma(2,3)
    5
    >>> soma(10,20)
    30
    >>> soma(5,1)
    6
    """
    return n1 + n2

if __name__ == "__main__":
    doctest.testmod()
    