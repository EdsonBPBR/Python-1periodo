# Crie um programa que recebe e armazena as números inteiros em uma fila. 
# Esse programa deve ter as funcionalidades:
# push: Insere um valor na lista.
# pop: Remove o valor mais antigo da lista.
# sum: Exibe a soma de todos os elementos da lista.
# print: exibe os valores contidos na lista em ordem de inserção.
# exit: encerra o programa
registro = []

while True:
    try:
        entrada = str(input()).split()
        if entrada == 'exit':
            break
        
        acao = entrada[0]
        elemento = int(entrada[1])
        
        if acao == 'push':
            registro.append(elemento)

    except IndexError:
        if acao == 'exit':
            break
        
        if acao == 'print':
            for posicao in range(len(registro)):
                print(registro[posicao], end=' ')
            print()

        elif acao == 'pop':
            registro.pop(0)
        
        elif acao == 'sum':
            print(int(sum(registro)))
        
        else:
            print('Entrada Inválida!')    