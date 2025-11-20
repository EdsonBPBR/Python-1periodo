from aluno import Aluno
from sistema_alunos import SistemaAlunos

sistema = SistemaAlunos()
def menu():
    print(f'\n{'='*8}SISTEMA ALUNOS{'='*8}')
    print(f'1. CADASTRAR ALUNO')
    print(f'2. LISTAR ALUNOS')
    print(f'3. BUSCAR ALUNO')
    print(f'4. SAIR')
    try:
        opc = int(input(': '))
        return opc
    except:
        print('Dado de entrada inválido!') 

def sistema_cadastrar_aluno():
    try:
        print(f'\n{'='*8}CADASTRAR ALUNO{'='*8}')
        matricula = str(input('Matricula: ')) 
        if sistema.busca_aluno(matricula) == None:
            nome = str(input('Nome completo: '))
            idade = int(input('Idade: '))
            email = str(input('Validar e-mail: ')) # futuramente validar e-mail
            # implementar sistema para verificar matricula
            aluno = Aluno(matricula, nome, idade, email)
            sistema.cadastrar_aluno(aluno)
        else:
            print('Discente já cadastrado!')
    except ValueError:
        print('Dado de entrada inválido!')

def sistema_listar_alunos():
    print(f'\n{'='*8}LISTAR ALUNOS{'='*8}')
    for aluno in sistema.listar_alunos():
        print(aluno)
    
def sistema_buscar_aluno():
    print(f'\n{'='*8}CADASTRAR ALUNO{'='*8}')
    matricula = str(input('Matricula: '))
    
    if sistema.busca_aluno(matricula) == None:
        print('Discente não cadastrado!')
    else:
        print(sistema.busca_aluno(matricula))

def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                sistema_cadastrar_aluno()
                
            case 2:
                sistema_listar_alunos()
        
            case 3:
                sistema_buscar_aluno()
                    
            case 4:
                print('Saindo do programa...')
                break
            case _:
                print('Opção Inválida!')
                
if __name__ == '__main__':
    main()