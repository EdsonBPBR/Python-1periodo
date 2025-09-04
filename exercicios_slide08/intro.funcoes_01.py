def paridade(valor): #funções sem retornos são funções de procedimento, e funções com retorno são funções com retorno.
    if (valor % 2 == 0):
        return 'PAR'
    else:
        return 'ÍMPAR'

#main
if __name__ == '__main__':

    while True:
        n = int(input())

        if n == -1:
            break

        print(paridade(n))

# class Mulher:
#     def __init__(self, nome, cpf, tamanho, peso, cor, raca, cozinhar, posicao_preferida, faz_academia):
#         self.nome = nome
#         self.cpf = cpf
#         self.tamanho = tamanho
#         self.peso = peso 
    