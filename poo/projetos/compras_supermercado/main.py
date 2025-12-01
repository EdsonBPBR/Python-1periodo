from produto import Produto
from sistema_produtos import SistemaProdutos
import os
sistema = SistemaProdutos()

def menu():
    print(f'\n{'='*10}MENU{'='*10}')
    print(f'1. {'CADASTRAR PRODUTO':<20}')
    print(f'2. {'LISTAR PRODUTOS':<20}')
    print(f'3. {'REMOVER PRODUTO':<20}')
    print(f'4. {'VALOR TOTAL':<20}')
    print(f'5. {'SAIR SISTEMA':<20}')
    try:
        opc = int(input(': '))
        return opc
    except ValueError:
        print('Dado de entrada inválido!')

def validar_codigo(codigo):
    if codigo.isdigit() and len(codigo) < 5 and sistema.busca_codigo(codigo):
        return True
    return False

def cadastrar_produto():
    os.system('cls')
    print(f'\n{'='*10}CADASTRAR PRODUTO{'='*10}')
    try:
        codigo = str(input('Código: '))
        if validar_codigo(codigo):
            nome = str(input('Nome: '))
            valor = float(input('Preco (R$): '))
            quantidade = int(input('Quantidade (uni): '))
            sistema.inserir_produto(Produto(codigo, nome, valor, quantidade))
            print(f'\n✅ Produto Cadastrado!')
            input('pressione ENTER para continuar\n')
        else:
            print('Código Inválido ou já existente!')
            input('pressione ENTER para continuar\n')  
    except ValueError:
        print('Dado de entrada inválido!')

def exibir_produtos():
    os.system('cls')
    print(f'\n{'='*15}PRODUTOS CADASTRADOS{'='*15}')
    print(f'# {'CODIGO':^10}{'NOME':^10}{'VALOR(R$)':^11}{'QUANTIDADE':^10}{'TOTAL':^10}')
    print(f'{'='*50}')
    for i, registros in enumerate(sistema.listar_produtos_cadastrados()):
        print(f'{i+1} {registros['codigo']:^10} {registros['nome']:^10} {registros['valor']:^10} {registros['quantidade']:^5} {registros['total']:^12}')
    input('Pressione ENTER para continuar\n')

def sistema_remover_produto():
    os.system('cls')
    print(f'\n{'='*15}REMOVER PRODUTO{'='*15}')
    codigo = str(input('Código: '))
    if sistema.remover_produto(codigo):
        print('Produto removido com sucesso!\n')
    else:
        print('Produto não encontrado!\n')
    input('Pressione ENTER para continuar\n')

def exibir_total():
    os.system('cls')
    print(f'\n{'='*15}TOTAL PRODUTOS (R$){'='*15}')
    print(f'R$ {sistema.calculo_total():.2f}\n')
    input('Pressione ENTER para continuar\n')
    
def main():
    while True:
        os.system('cls')
        opc = menu()
        match opc:
            case 1:
                cadastrar_produto()
                    
            case 2:
                exibir_produtos()
                
            case 3:
                sistema_remover_produto()
                
            case 4:
                exibir_total()
                
            case 5:
                print('Saindo do sistema...')
                break
            
            case _:
                print('Opção inválida!')
                
if __name__ == '__main__':
    main()