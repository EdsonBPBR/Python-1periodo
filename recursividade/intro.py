# funmção iterativa, sem recursividade:
# def fatorial(n):
#     fat = 1
#     for i in range(1, n+1):
#         fat *= i
#     return fat
# print(fatorial(1))

#backtracking, algoritmo utilizado em IA

# funcao recursiva
def fatorial(n):
    if n == 1 or n == 0: 
        return 1 # condição de parada ou condição de escape
    elif n > 1:
        return n * fatorial(n-1)
    # possui uma chamada recursiva, chama a própria função
# em funções recursivas é fundamental a condição de escape, senão a função entrará em loop infinito

if __name__ == '__main__':
    try:
        m = int(input())
        print(fatorial(m))
    except ValueError:
        print('Valor de entrada inválido!')
