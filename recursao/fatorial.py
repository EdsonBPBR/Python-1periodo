def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fatorial(n-1) * n
    
def main():
    n = int(input('Informe um número: '))
    print(fatorial(n))

if __name__ == '__main__':
    main()