if __name__ == '__main__':
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
                if len(registro) > 0:
                    registro.pop(-1)
            
            elif acao == 'sum':
                print(int(sum(registro)))
            
            elif acao == 'average':
                if len(registro) < 1:
                    media = 0
                    print(f'{media:.2f}')
                else:
                    media = (sum(registro)) / (len(registro))
                    print(f'{media:.2f}')

            elif acao == 'pow':
                for posicao in range(len(registro)):
                    print(registro[posicao]**2, end=' ')
                print()
            
            else:
                print('Entrada Inválida!')    