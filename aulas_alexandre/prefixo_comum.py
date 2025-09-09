nome1 = str(input())
nome2 = str(input())

semelhanca = ''

lista_nome1 = list(nome1)
lista_nome2 = list(nome2)

a = len(lista_nome1)
b = len(lista_nome2)

if a != b:
    if a > b:
        while b < a:
            lista_nome2.append('')
            b += 1
    else:
        while a < b:
            lista_nome1.append('')
            a += 1

    for x in range(a):
        if lista_nome1[x] == lista_nome2[x]:
            semelhanca += f'{lista_nome1[x]}'
        else:
            break
else:
    for x in range(a):
        if lista_nome1[x] == lista_nome2[x]:
            semelhanca += f'{lista_nome1[x]}'
        else:
            break
            
print(semelhanca)

## tamanho
#laço de repetição, se o elemento de lá for igual, então armazenar em uma string vazia
