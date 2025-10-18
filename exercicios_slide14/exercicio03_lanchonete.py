# Crie um programa para gerenciar uma lanchonete, cada produto possui um Nome e
# um Valor, o programa deve permitir:
# 1 Salvar produtos
# 2 Listar produtos

# id, nome, valor # id único para poder identificar cada produto, evitar redundância, interferências (alterações indesejadas...)
import os
import json
from uuid import uuid1

def menu():
    os.system('cls')
    print('1 - CADASTRAR PRODUTO')
    print('2 - LISTAR PRODUTOS')
    print('3 - EDITAR PRODUTO')
    print('0 - SAIR')

def cadastrarProduto(registro):
    try:
        with open('exercicios_slide14/arquivos_lanchonete/produtos.json', 'r') as arquivo:
            dados = json.load(arquivo) # não utiliza o parâmetro 'a', primeiro guarda todos os registros na variavel dados e, em seguida, vai incrementando os dadoos
    except (FileNotFoundError, json.JSONDecodeError):
        dados = []
        
    dados.append(registro)
    with open('exercicios_slide14/arquivos_lanchonete/produtos.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        # ident serve para identar o json, deixar formatado ao invés de em uma linha
    
    print('Produto cadastrado com sucesso!\n')
    input('Pressine ENTER para continuar...')
        
def imprimirProdutosCadastrados():
    os.system('cls')
    with open('exercicios_slide14/arquivos_lanchonete/produtos.json', 'r') as arquivo:
        documento = json.load(arquivo)
        
    for posicao in range(len(documento)):
        print(f'{documento[posicao]['id']}. {documento[posicao]['nome']}')
        
        if posicao + 1 == len(documento):
            print(f'Preco: R${documento[posicao]['valor']}\n')
        else:
            print(f'Preco: R${documento[posicao]['valor']}')
    
while True:
    menu()
    try:
        opc = int(input('Opção: '))
        
        match opc:
            case 1:
                os.system('cls')
                print('Cadastrar Produto')
                id = str(uuid1())
                nome = str(input('Nome: ')).strip().upper()
                valor = float(input('Valor(R$): '))
                
                registro = {
                    'id': id,
                    'nome': nome,
                    'valor': valor
                }
                cadastrarProduto(registro)
                
            case 2:
                imprimirProdutosCadastrados()
                input('Pressione ENTER para continuar')
                
            case 3:
                pass
            
            
            case 0:
                print('Saindo do programa...')
                break

            case _:
                print('Opção Inválida!')
                
    except ValueError:
        print('Dado de entrada inválido! Selecione uma das opções (0-3)\n')
        input('Pressione ENTER para continuar')