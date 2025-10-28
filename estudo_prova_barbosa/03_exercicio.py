registros = []
controle_matriculas = set()

def menu():
    print('1 - Cadastrar Discente')
    print('2 - Visualizar Discentes')
    print('3 - Sair')

def cadastrarDiscente(matricula, nome, controle_matriculas):
    registros.append((matricula, nome))
    controle_matriculas.add(matricula)
    
def imprimirSaida(registros):
    print(f"{'='*20}")
    print(f"{'Matricula':<15} {'Nome':<15}")
    print(f"{'='*20}")
    for tupla in registros:
        print(f'{tupla[0]:<5}. {tupla[1]:^20}')

def main():
    while True:
        menu()
        opc = int(input("Opção: "))
        
        match opc:
            case 1:
                matricula = int(input('Matrícula: ')) #poderia inserir uma estrutura de tratamento, utilizando to try
                if matricula in controle_matriculas:
                    print('Discente já cadastrado!')
                    
                else:
                    nome = str(input('Nome: '))
                    cadastrarDiscente(matricula, nome, controle_matriculas)
                    print('Discente cadastradom com sucesso!')
                
            case 2:
                imprimirSaida(registros)
                
            case 3:
                print('Saindo do programa...')
                break
            
            case _:
                print('Opção Inválida! Tente novamente.')
                
if __name__ == '__main__':
    main()