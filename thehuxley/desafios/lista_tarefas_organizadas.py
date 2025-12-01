def cadastrar_tarefa(registros, i):
    descricao = input().strip()
    prioridade = int(input())
    registros[prioridade].append((i, descricao))
    registros[prioridade].sort(key=lambda item:(item[0]), reverse=True)

def exibir_tarefas(registros):
    for chave in registros.keys():
            for registro in registros[chave]:
                print(f'{chave}. {registro[1]}')
    print()

def main():
    i = 0
    registros = {
        1:[],
        2:[],
        3:[],
        4:[],
        5:[]
    }

    while True:
        try:
            opc = int(input())
            if opc == 0:
                break
            elif opc == 1:
                cadastrar_tarefa(registros, i)
                i += 1 
            elif opc == 2:
                exibir_tarefas(registros)
        except:
            print('Estamos com problemas na conexão com o servidor')
            
if __name__ == '__main__':
    main()