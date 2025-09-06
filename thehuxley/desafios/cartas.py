def verifica_lista(lista_usuario, lista_crescente, lista_decrescente):
    if lista_usuario == lista_crescente:
        return 'C'

    elif lista_usuario == lista_decrescente:
        return 'D'

    else:
        return 'N'

lista_ordenada_crescente = []
lista_ordenada_decrescente = []

v1, v2, v3, v4, v5 = map(int, input().split())
lista_usuario = [v1, v2, v3, v4, v5]

for a in lista_usuario:
    lista_ordenada_crescente.append(a)
    lista_ordenada_decrescente.append(a)
    
lista_ordenada_crescente.sort()
lista_ordenada_decrescente.sort(reverse=True)

print(verifica_lista(lista_usuario, lista_ordenada_crescente, lista_ordenada_decrescente))
