# Luigi ganhou uma mochila nova com capacidade para transportar até 18 kg. Como tem muitos livros, ele deseja descobrir quantos podem ser levados na mochila sem exceder esse limite.
# Escreva um programa que receba como entrada o peso de vários livros de Luigi e exiba a quantidade de livros que podem ser carregados.

capacidade = 18
n_livros = 0
while True:
    peso_livro = int(input())
    
    if peso_livro <= capacidade:
        capacidade -= peso_livro
        n_livros += 1
    else:
        break
    
print(n_livros)

    
    