# Crie um programa para salvar nome e matricula de discentes de uma disciplina
import os

def menu():
    print('1 - CADASTRAR DISCENTE')
    print('2 - VISUALIZAR PÁGINA DISCENTES')
    print('3 - VISUALIZAR REGISTRO DISCENTES')
    print('0 - MENU')

def cadastrarDiscente(registro):
    caminho_arquivo = os.path.join('exercicios_slide14', 'arquivos', 'registro_discentes.txt')
    
    if not os.path.exists(caminho_arquivo):
        criarArquivo()
        
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(registro)

def visualizarPaginaDiscentes():
    caminho_arquivo = os.path.join('exercicios_slide14', 'arquivos', 'registro_discentes.txt')
    
    if not os.path.exists(caminho_arquivo):
        criarArquivo()
    
    with open(caminho_arquivo, 'r') as arquivo:
        pagina_completa = arquivo.read()
        print(pagina_completa)
        
def visualizarRegistrosDiscentes():
    caminho_arquivo = os.path.join('exercicios_slide14', 'arquivos', 'registro_discentes.txt')
    
    if not os.path.exists(caminho_arquivo):
        criarArquivo()
        
    with open(caminho_arquivo, 'r') as arquivo:
        linhas_arquivos = arquivo.readlines()
        for registros in range(3, len(linhas_arquivos)):
            print(linhas_arquivos[registros].split())
            
def criarArquivo():
    with open('exercicios_slide14/arquivos/registro_discentes.txt', 'w') as arquivo:
        arquivo.write('='*15 + 'ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES' + '='*15+'\n')
        arquivo.write('MATRICULA                             NOME\n')
        arquivo.write('='*72+'\n')
        
    print('Arquivo de registros criado com sucesso!')

if __name__ == '__main__':
    while True:
        os.system('cls')
        menu()
        try:
            opc = int(input('Opção: '))
        
            match opc:
                case 0:
                    print('Saindo do programa...')
                    break            
                
                case 1:
                    nome = str(input('Nome: ')).upper()
                    matricula = int(input('Matricula: '))
                    registro = f'{matricula:<35}. {nome:<50}\n'
                    cadastrarDiscente(registro)
                        
                case 2:
                    os.system('cls')
                    visualizarPaginaDiscentes()
                
                    input('Pressione ENTER para continuar')
                    
                case 3:
                    os.system('cls')
                    visualizarRegistrosDiscentes()
                    
                    input('Pressione ENTER para continuar...')
                
                case _:
                    print('Entrada Inválida!')
                    
        except ValueError:
            print('Dado de Entrada Inválido! Tente novamente!')
            input('Pressione ENTER para continuar...')