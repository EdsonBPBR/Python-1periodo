# Programa que determina o preço com desconto para entradas de cinema.

# Estudantes recebem 50% de desconto, aposentados, 30%. Os demais clientes pagam o valor integral.
# def verificaEntrada(cat_cliente, preco):

#     if cat_cliente.upper() == 'E':
#         preco_final = preco * 0.5
#         status = 'com'
#         cat = 'Estudante'

#         return preco_final, status, cat
    
#     elif cat_cliente.upper() == 'A':
#         preco_final = preco * 0.7
#         status = 'com'
#         cat = 'Aposentado'

#         return preco_final, status, cat
    
#     elif cat_cliente.upper() == 'N':
#         preco_final = preco
#         status = 'sem'
#         cat = None

#         return preco_final, status, cat

#     else:
#         return ('Categoria invalida!')

if __name__ == '__main__':
    preco = float(input())
    cat_cliente = str(input())

    if cat_cliente.upper() == 'E':
        preco_final = preco * 0.5
        status = 'com'
        cat = 'Estudante'
        print(f'Preco {status} desconto: R${preco_final:.2f}')
        print(f'Categoria: {cat}')

    elif cat_cliente.upper() == 'A':
        preco_final = preco * 0.7
        status = 'com'
        cat = 'Aposentado'

        print(f'Preco {status} desconto: R${preco_final:.2f}')
        print(f'Categoria: {cat}')

    elif cat_cliente.upper() == 'N':
        preco_final = preco
        status = 'sem'
    
        print(f'Preco {status} desconto: R${preco_final:.2f}')

    else:
        print('Categoria invalida!')

    