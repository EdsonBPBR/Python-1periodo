# A primeira linha da entrada consiste de um número K representando o número de jogos que serão realizados.
# próxima linha consiste de um número N, [0 < N < 8], representando o tamanho da senha a ser utilizada no próximo jogo.
# A próxima linha contém uma senha contendo dígitos, entre 1 e 7, 
# As próximas linhas contêm os chutes dados pelo segundo jogador e, portanto, consistem de uma sequência de dígitos, entre 1 e 7, com exatamente N caracteres
# Cada jogo termina quando a senha é acertada ou quando o jogador desiste de tentar digitando uma seqüência de N caracteres '0'.


k = int(input()) # número de jogos

for a in range(k):
    n = int(input()) # tamanho da senha
    entrada_senha = str(input())
    senha = list(entrada_senha)
    
    while True:
        tentativa = str(input())
        
        # for elemento in tentativa:
        #     print(elemento in senha)

        if tentativa == f'{'0'*n}':
            break
        
        x = 0
        for i in range(n):
            if tentativa[i] == senha[i]:
                x += 1

        y = 0
        senha_restante = []
        for i in range(n):
            if tentativa[i] != senha[i]:
                senha_restante.append(senha[i])

        for i in range(n):
            if tentativa[i] != senha[i] and tentativa[i] in senha_restante:
                y += 1
                senha_restante.remove(tentativa[i])
                        
        print(f'({x},{y})')
        if x == n and y == 0:
            break