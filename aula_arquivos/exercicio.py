while True:
    print('1 - CADASTRAR DISCENTE')
    print('2 - VISUALIZAR CADASTRADOS')
    print('0 - SAIR')
    
    opc = int(input())
    
    match opc:
        case 1:
            n_alunos = int(input('Informe o número de discentes: '))
            registros = []
            
            for _ in range(n_alunos):
                nome = str(input("Nome: "))
                matricula = int(input("Matricula: "))
                registros.append((nome, matricula))
                
                with open("aula_arquivos/apc.txt", "w") as arquivo:
                    arquivo.write('ALGORITMOS E PROGRAMACAO DE COMPUTADORES \n')
                    
                    for k in range(len(registros)):
                        arquivo.write(f'{registros[k][0]}, {registros[k][1]} \n')
        case 2:
            with open('aula_arquivos/arquivos.txt', "a") as arquivo:
                
        case 0:
            break
        case _:
            print('Opção Inválida!')
            
            input('Pressione ENTER para continuar')