# Crie um programa para realizar matriculas em uma disciplina. Discentes possuem um nome e uma matricula, a matricula  ́e  ́unica para cada discente. Deve sera presentada tamb ́em a op ̧c ̃ao de listar os discentes matriculados. O programa
# permanece em execu ̧c ̃ao at ́e que o usu ́ario deseje finalizar.
import os

def menu():
    print('1 - CADASTRAR DISCENTE')
    print('2 - ALTERAR DISCENTE')
    print('3 - VISUALIZAR DISCENTES')
    print('0 - SAIR')

registros = {}

while True:
    os.system('cls')
    menu()
    opc = int(input(": "))
    
    match opc:
        case 0:
            break
        
        case 1:
            matricula = int(input('Matricula: '))
            
            if not(matricula in registros):
                nome_completo = str(input('Nome completo: ')).upper()
                registros[matricula] = nome_completo
                
                print('Discente cadastrado com sucesso! \n')
                input('Pressione ENTER para continuar \n')
                
            else:
                print('Discente já cadastrado! \n')
                input('Pressione ENTER para continuar \n')
        
        case 2:
            matricula = int(input('Matricula: '))
            
            if matricula in registros:
                nome_completo = str(input('Novo nome: ')).upper()
                registros[matricula] = nome_completo
                
                print('Dados do discente alterados com sucesso! \n')
                input('Pressione ENTER para continuar \n')
                
            else:
                print('Discente não cadastrado! \n')
                input('Pressione ENTER para continuar \n')
        
        case 3:
            # print(registros)
            print('='*54)
            print(f'{'ID':^5}{'NOME':^45}')
            print('='*54)
            for chave, nome in registros.items():
                print(f'|{chave:^5}. {nome:^45}|')
            print('='*54)
            print()
            
            input('Pressione ENTER para continuar \n')
            
        case _ :
            print('Opção Inválida! \n')
            input('Pressione ENTER para continuar \n')