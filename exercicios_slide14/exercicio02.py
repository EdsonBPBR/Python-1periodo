# Crie um programa para salvar nome e matricula de discentes de uma disciplina,
# considerando que em um mesmo diret ́orio sejam fornecidos arquivos no formato .txt.
# Cada arquivo cont ́em na sua primeira linha o nome da disciplina e nas linhas
# posteriores os nomes e matriculas dos discentes matriculados
# eu não irei me preocupar com a verificação se o arquivo .txt de cada disciplina foi ou não criado. Ele já deve, por padrão, está no diretório previamente criado.
# ICC, SOCC, DD, APC, FM, LAC
import os

opc = {
    1:'icc.txt', 
    2:'socc.txt', 
    3:'dd.txt', 
    4:'apc.txt', 
    5:'fmat.txt', 
    6:'lac.txt'}

def menu():
    print('1 - CONSULTAR DISCIPLINAS')
    print('2 - CADASTRAR ALUNO EM DISCIPLINA')
    print('3 - EDITAR ALUNO')
    print('0 - SAIR')

def disciplinasDisponiveis():
    print('1 - Intro. Ciência da Computação (ICC)')
    print('2 - Sociedade e Cultura (SOCC)')
    print('3 - Direito Digital (DD)')
    print('4 - Alg. e Programação (APC)')
    print('5 - Fundamentos da Matemática (FM)')
    print('6 - Log. Aplicada em Computação (LAC) \n')

def exibirDisciplina(disciplina, opc = opc):
    os.system('cls')
    with open(f'exercicios_slide14/arquivos_exercicio02/{opc[disciplina]}', 'r') as arquivo:
        documento = arquivo.read()
        print(documento + '\n')
    
    input('Pressione ENTER para continuar...')
    
def cadastrarAluno(disciplina, registro, opc = opc):
    os.system('cls')
    with open(f'exercicios_slide14/arquivos_exercicio02/{opc[disciplina]}', 'a') as arquivo:
        arquivo.write(registro)
    print('Aluno cadastrado com sucesso!')
    
    input('Pressione ENTER para continuar...')

def entradaCadastroAluno():
    matricula = int(input('Matricula: ')) # inserir uma estrutura de tratamento do tipo de dados e limites, por exemplo, tamanho da matrícula, se é válida, se não é válida, enfim....
    nome = str(input('Nome: ')).upper()
    registro = f'{matricula:<25}. {nome:<25}\n'
                        
    cadastrarAluno(sub_opc, registro)
    
    
if __name__ == '__main__':
    while True:
        os.system('cls')
        menu()
        
        try:
            opc = int(input("Opção: "))
            match opc:
                case 1:
                    os.system('cls')
                    print('DISCIPLINAS DISPONÍVEIS: ')
                    disciplinasDisponiveis()
                    sub_opc = int(input("Selecione a Disciplina: "))
                    
                    if not(sub_opc >= 1 and sub_opc <= 6):
                        while True:
                            print('Opção Inválida! Tente novamente...')
                            sub_opc = int(input("Selecione a Disciplina: ")) # futuramente inserir uma estrutura de tratamento, quiando 
                            
                            if sub_opc >= 1 and sub_opc <= 6:
                                exibirDisciplina(sub_opc)
                                break
                    else:
                        exibirDisciplina(sub_opc)
                        
                case 2:
                    os.system('cls')
                    print('DISCIPLINAS DISPONÍVEIS: ')
                    disciplinasDisponiveis()
                    
                    sub_opc = int(input("Selecione a Disciplina: "))
                    
                    if not(sub_opc >= 1 and sub_opc <= 6):
                        while True:
                            print('Opção Inválida! Tente novamente...')
                            sub_opc = int(input("Disciplina: ")) # futuramente inserir uma estrutura de tratamento, quiando 
                            
                            if sub_opc >= 1 and sub_opc <= 6:
                                entradaCadastroAluno()
                                break
                    else:
                        entradaCadastroAluno()

                case 3:
                    os.system('cls')
                    print('DISCIPLINAS DISPONÍVEIS: ')
                    disciplinasDisponiveis()
                    sub_opc = int(input("Selecione a Disciplina: "))
                    
                    if not(sub_opc >= 1 and sub_opc <= 6):
                        while True:
                            print('Opção Inválida! Tente novamente...')
                            sub_opc = int(input("Disciplina: ")) # futuramente inserir uma estrutura de tratamento, quiando 
                            
                            if sub_opc >= 1 and sub_opc <= 6:
                                pass
                    else:
                        matricula = str(input('Matricula: ')).strip() # inserir sistema verificação da matricula
                         
                        with open('exercicios_slide14/arquivos_exercicio02/icc.txt', 'r') as arquivo:
                            linhas = arquivo.readlines()
                            
                            freq = False
                            for posicao_elemento_cadastrado in range(5, len(linhas)):
                                if matricula in linhas[posicao_elemento_cadastrado]:
                                    registro = linhas[posicao_elemento_cadastrado].split()
                                    
                                    novo_nome = str(input(f'Informe o novo nome do usuário {registro[2]}: '))
                                    freq = True 
                                    
                                    # ainda tenho que terminar esse bloco de código, aplicar a mudança no arquivo .txt, eu ainda irei verificar isso.
                                    
                            if not(freq):
                                print('Usuário não encontrado!')
                                
                        input('Pressione ENTER para continuar...')

                case 0:
                    print('Saindo do programa...')
                    break
                
                case _:
                    print('Opção Inválida! \n')
                    input('Pressione ENTER para continuar...')
                    
        except ValueError:
            print('Dado de entrada Inválido! Tente novamente... \n')
            input('Pressione ENTER para continuar...')