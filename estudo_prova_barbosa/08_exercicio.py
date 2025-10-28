
# é necessário que a própria biblioteca pickle crie o arquivo, não dá certo se criar manualmente!
import pickle
# with open('estudo_prova_barbosa/dados.dat', 'wb') as arquivo:
#     pickle.dump([],arquivo)

import os

def menu():
    print('1 - Cadastrar Discente')
    print('2 - Visualizar Discentes cadastrados')
    print('3 - Sair')
    opc = int(input('Opção: '))
    return opc

def extrairDados():
    with open('estudo_prova_barbosa/dados.dat', 'rb') as arquivo:
        registros = pickle.load(arquivo)    
    return registros

def gravarDados(registros_atualizados):
    with open('estudo_prova_barbosa/dados.dat', 'wb') as arquivo:
        pickle.dump(registros_atualizados, arquivo)  

def imprimirSaida(dados):
    print(f"{'===ALGORITMOS E PROGRAMAÇÃO===':^20}")
    print(f"{'MATRICULA                 NOME':^20}")
    for registro in dados:
        print(f'{registro[1]:>5}. {registro[0]:>23}')   
    input('pressione ENTER para continuar')

registros = extrairDados()
controle_matriculas = set()

for matricula in registros:
    controle_matriculas.add(matricula[1])

while True:
    os.system('cls')
    opc = menu()
    match opc:
        case 1:
            matricula = int(input('Matricula: '))
            
            if matricula in controle_matriculas:
                print('Discente já cadastrado!\n')
                
            else:
                nome = str(input('Nome: ')).title()
                registros.append([nome, matricula])
                controle_matriculas.add(matricula)
                gravarDados(registros)
                print('Discente cadastrado com sucesso!\n')
                
            input('pressione ENTER para continuar')
            
        case 2:
            dados = extrairDados()
            imprimirSaida(dados)
            
        case 3:
            print('Saindo do programa...')
            break
        
        case 4:
            print('Opção Inválida!')