import os
def menu():
    print('1 - INSERIR')
    print('2 - REMOVER')
    print('3 - LISTAR')
    print('0 - SAIR')
    
def main():
    lista_compras = []
    while True:
        os.system('cls')
        menu()
        opc = int(input(": "))
        
        match opc:
            case 0:
                print('Saindo do programa...')
                break
            
            case 1:
                os.system('cls')
                print(f'{'INSERIR PRODUTO':^50}\n')
                
                nome = str(input('Nome: '))
                valor_uni = float(input('Valor (R$): '))
                quantidade = int(input('Quantidade: '))
                
                print('Produto cadastrado com sucesso!')
                lista_compras.append((nome, valor_uni, quantidade)) # poderia utilizar o dicionario
                
            case 2:
                os.system('cls')
                print(f'{'REMOVER PRODUTO':^50}\n')
                
                nome_item = str(input('Nome item cadastrado: ')).strip()
                freq = False
                
                for chave, valor in enumerate(lista_compras):
                    if valor[0] == nome_item:
                        freq = True
                        chave_remocao = chave
                
                if not(freq):
                    print('Produto não encontrado')
                else:
                    lista_compras.pop(chave_remocao)
                    print('Produto removido com sucesso!')
        
            case 3:
                os.system('cls')
                print(f'{'LISTAR PRODUTOS':^50}\n')
                
                total = 0
                for chave, valor in enumerate(lista_compras):
                    if len(lista_compras) - 1 == chave:
                        print(f'{chave+1}. {valor[0]} {valor[2]} x R$ {valor[1]:.2f} = R$ {(float(valor[2])*float(valor[1])):.2f}\n')
                    else:
                        print(f'{chave+1}. {valor[0]} {valor[2]} x R$ {valor[1]:.2f} = R$ {(float(valor[2])*float(valor[1])):.2f}')
                        
                    total += float(valor[2])*float(valor[1])
            
            
                print(f'Total: R$ {total:.2f}')
                input('Pressione ENTER para continuar...')
                
            case _:
                print('Opção Inválida! Tente novamente!')
                
if __name__ == '__main__':
    main()