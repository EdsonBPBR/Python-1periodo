n = int(input())
lista = []
for _ in range(n):
    livro = str(input())
    lista.append(livro)
    
livro_pesquisado = str(input())
presente = False
for elemento in lista:
    if elemento == livro_pesquisado:
        presente = True
        
if presente:
    print('Sim')
else:
    print('Não')