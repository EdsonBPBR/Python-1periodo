import pickle
# with open('estudo_prova_barbosa/lista_produtos.dat', 'wb') as arquivo:
#     pickle.dump([], arquivo)
import os
def menu():
    os.system('cls')
    print('1 - Inserir produto')
    print('2 - Listar produtos')
    print('3 - Remover produto')
    print('4 - Sair')
    opc = int(input('Opção: '))
    return opc

def extrairDados():
    with open('estudo_prova_barbosa/lista_produtos.dat', 'rb') as arquivo:
        dados = pickle.load(arquivo)
    return dados

def salvarDados(dados_atualizados):
    with open('estudo_prova_barbosa/lista_produtos.dat', 'wb') as arquivo:
        pickle.dump(dados_atualizados, arquivo)

def cadastrarProduto(dados):
    os.system('cls')
    print('INSERIR')
    nome = str(input('Nome: ')).strip()
    valor_uni = float(input('Valor uni(R$): '))
    quant = int(input('Quantidade: '))
    
    dados.append([nome, valor_uni, quant])
    salvarDados(dados)
    print('Produto inserido com sucesso!\n')
    input('pressione ENTER para continuar...')

def imprimirSaida(dados):
    os.system('cls')
    print('LISTAR')
    dados = extrairDados()
    total = 0
    for registro in dados:
        print(f'{registro[0]}, {registro[2]} UNI x R$ {registro[1]:.2f} = R$ {(registro[2])*(registro[1]):.2f} ')
        total += (registro[2])*(registro[1])
        
    print(f'Total = R$ {total:.2f}')
    input('pressione ENTER para continuar...')

def removerRegistro(dados):
    os.system('cls')
    print('REMOVER')
    
    nome_produto = str(input('Nome produto cadastrado: ')).strip()
    cadastrado = False
    for i, registro in enumerate(dados):
        if registro[0] == nome_produto:
            cadastrado = True
            item = i
    if cadastrado:
        print(f'Item: {dados[item]} removido com sucesso!\n')
        dados.pop(item)
        salvarDados(dados)
    
    else:
        print('Item não encontrado na base de dados\n')

    input('pressione ENTER para continuar...')
    
def main():
    while True:
        try:
            opc = menu()
            try:
                dados = extrairDados()
            except FileNotFoundError or UnboundLocalError:
                print('Não foi possível ler a base de dados ou está corrompida!\n')
                
            match opc:
                case 1:
                    cadastrarProduto(dados)
                    
                case 2:
                    imprimirSaida(dados)
                        
                case 3:
                    removerRegistro(dados)
                    
                case 4:
                    print('Saindo do programa...')
                    break
                
                case _:
                    print('Opção Inválida!\n')
                    input('pressione ENTER para continuar...')
                
        except ValueError:
            print('Dado de entrada inválido! Tente novamente informando um número inteiro\n')
            input('pressione ENTER para continuar...')     
            
if __name__ == '__main__':
    main()