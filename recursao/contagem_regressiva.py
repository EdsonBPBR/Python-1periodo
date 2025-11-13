def contagemRegresiva(n):
    if n == 0:
        return 0 # condição de escape (condição base)
    else:
        print(n, end = ' ')
        return contagemRegresiva(n-1)

def main():
    try:
        n = int(input('Entrada: '))
        print(contagemRegresiva(n))
    except ValueError:
        print('Valor de entrada inválido!')

if __name__ == '__main__':
    main()