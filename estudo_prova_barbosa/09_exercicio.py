import pickle

# with open('estudo_prova_barbosa/apc.dat', 'wb') as arquivo:
#     pickle.dump(['Algoritmos e Programação de Computadores'], arquivo)
    
# with open('estudo_prova_barbosa/icc.dat', 'wb') as arquivo:
#     pickle.dump(['Introdução à Ciência da Computação'], arquivo)

def menu():
    print('1 - Inserir Discente')
    print('2 - Listar Disciplina')
    print('3 - Sair')
    opc = int(input('Opção: '))
    return opc
    
def submenu():
    print('1 - Algoritmos e Programação de Computadores')
    print('2 - Introdução a Ciência da Computação')
    sub_opc = int(input('Disciplina: '))
    return sub_opc

def extrairDados(sub_opc):
    disciplinas = {
        1:'apc',
        2:'icc'
        }
    with open(f'estudo_prova_barbosa/{disciplinas[sub_opc]}.dat', 'rb') as arquivo:
        dados = pickle.load(arquivo)
    return dados

def salvarDados(sub_opc, dados_atualizados):
    disciplinas = {
        1:'apc',
        2:'icc'
        }
    with open(f'estudo_prova_barbosa/{disciplinas[sub_opc]}.dat', 'wb') as arquivo:
        pickle.dump(dados_atualizados, arquivo)

def cadastrarDiscente(subopc, nome, matricula):
    dados = extrairDados(subopc)
    cadastrado = False
    # verificar se discente está matriculado em disciplina
    for registro in dados:
        if registro[0] == matricula:
            cadastrado = True
    
    if cadastrado:
        print('Discente já cadastado em Disciplina!')
    else:
        dados.append([matricula, nome])
        salvarDados(subopc, dados)
        print('Discente matriculado com sucesso!')
    
def imprimirDisciplina(subopc):
    dados = extrairDados(subopc)
    for chave, registro in enumerate(dados):
        if chave == 0:
            print(f'{registro:^55}')
        else:
            print(f'{registro[0]:<20}. {registro[1]:<40}')  
             
def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                matricula = int(input('Matricula: '))
                nome = str(input('Nome: ')).strip().title()
                subopc = submenu()
                
                match subopc:
                    case 1:
                        cadastrarDiscente(subopc, nome, matricula) 
                    case 2:
                        cadastrarDiscente(subopc, nome, matricula)
                    case _:
                        print('Disciplina Inválida!')
                
            case 2:
                subopc = submenu()
                match subopc:
                    case 1:
                        imprimirDisciplina(subopc)
            
                    case 2:
                        imprimirDisciplina(subopc)
                        
                    case _:
                        print('Opção Inválida!')
            case 3:
                print('Saindo do programa')
                break
            case _:
                print('Opção Inválida!')
if __name__ == '__main__':
    main()