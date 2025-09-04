#não pode utilizar nesse caso, professor proibiu : (

def fatorial(n):
    c = 0
    calculo_fatorial = 1

    while n > c:
        calculo_fatorial = calculo_fatorial * (n - c)
        c = c + 1
        
    return calculo_fatorial

#main
if __name__ == '__main__':
    numero = int(input())
