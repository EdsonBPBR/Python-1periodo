# Crie um programa para gerenciar uma lanchonete, cada produto possui um Nome e
# um Valor, o programa deve permitir:
# 1 Salvar produtos
# 2 Listar produtos
# 3 Remover produto

import os
import pickle
# with open('estudo_prova_barbosa/dados_lanchonete.dat', 'wb') as arquivo:
#     pickle.dump([], arquivo)

def extrairDados():
    with open('estudo_prova_barbosa/dados_lanchonete.dat', 'rb') as arquivo:
        dados = pickle.load(arquivo) 
    return dados

def salvarDados(dados_atualizados):
    with open('estudo_prova_barbosa/dados_lanchonete.dat', 'wb') as arquivo:
        pickle.dump(dados_atualizados, arquivo) 

def menu():
    os.system('cls')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Remover Produto')
    print('4 - Sair')
    opc = int(input('Opção: '))
    return opc

def imprimirSaida(dados):
    os.system('cls')
    for registro in dados:
        print(f'{registro['id']}. {registro['nome']} - R$ {registro['valor']:.2f}')
    
    input('pressione ENTER para continuar')

def cadastrarProduto(id, dados ):
    nome = str(input('Nome: ')).strip().title()
    valor = float(input('Valor (R$): '))
    dados.append(
        {
        'id':id, 
        'nome': nome, 
        'valor': valor
        })
            
    salvarDados(dados)
    
def verificaProdutoCadastrado(id, dados):
    cadastrado = False
    for registro in dados:
        if registro['id'] == id:
            cadastrado = True
            posicao = registro
            
            return cadastrado, posicao
    
def main():
    while True:
        id = 0
        opc = menu()
        match opc:
            case 1:
                dados = extrairDados()
                for registro in extrairDados(): # controle dos ids
                    id += 1
                cadastrarProduto(id, dados)
                
            case 2:
                dados = extrairDados()
                imprimirSaida(dados)
                
            case 3:
                id = int(input('Informe o ID do produto: '))
                dados = extrairDados()
                cadastrado = False
                for registro in dados: # implementar também função
                    if registro['id'] == id:
                        cadastrado = True
                        posicao = registro
                    
                if cadastrado:
                    dados.pop(dados.index(registro))
                    salvarDados(dados)
                    print('Item removido com sucesso!')
                else:
                    print('Item não encontrado!')
                    
                input('pressione ENTER para continuar...')
            case 4:
                break
            case _:
                print('Opção inválida!')

if __name__ == '__main__':
    main()