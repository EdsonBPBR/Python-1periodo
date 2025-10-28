import os
# PROBLEMA PARCIALMENTE RESOLVIDO
def menu():
    os.system('cls')
    print(f'{'Menu':^25}')
    print('1 - Matricular Discente')
    print('2 - Visualizar Discente')
    print('3 - Sair')
    opc = int(input('Opção: '))
    return opc
    
def subMenu():
    os.system('cls')
    print(f'{'Cadastrar em Disciplina':^30}')
    print('1 - Intro. Ciência da Computação')
    print('2 - Direito Digital')
    print('3 - Alg. e Prog. de Computadores')
    print('4 - Fundamentos da Matemática')
    print('5 - Lógica Aplica em Computação')
    print('6 - Sociedade e Cultura')
    print('7 - Voltar')
    sub_opc = int(input('Subopção: '))
    return sub_opc

while True:
    opc = menu()
    match opc:
        case 1:
            matricula = int(input('Matricula: '))
            nome = str(input('Nome: ')).strip().title()
            
            sub_opc = subMenu()
            match sub_opc:
                case 1:
                    with open('dd.txt', 'r') as arquivo:
                        dados = arquivo.readlines()
                    print(dados)
                    input()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    print()
                case _:
                    print('Opção Inválida!!\n')
                    input('pressione ENTER para retornar ao menu principal')

        case 2:
            pass
        
        case 3:
            print('Saindo do programa...')
            break
    
