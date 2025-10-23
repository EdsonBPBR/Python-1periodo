# estou primeiramente estudando ou criando minha própria estrutura de dadosz
# lista = ['A','C', 'G', 'T', 'A']
lista = ['A','A', 'G', 'T', 'A', 'C', 'E', 'E']
t = len(lista)
registros = {}

for i in range(1, t+1):
    if not(lista[i-1] in registros): # verificar se existe no dicionário
        freq = 0
        for j in range(t):
            soma = j + i
            # print(soma%t)
            print(lista[soma%t])
            
            if lista[i-1] == lista[soma%t]:
                freq += 1
                
            registros[f'{lista[i-1] }'] = freq-1
            
        # print(freq-1)
        # print('-'*5)
print(registros)