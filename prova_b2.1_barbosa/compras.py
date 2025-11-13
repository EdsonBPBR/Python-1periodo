import pickle
# with open('prova_b2.1_barbosa/compras.dat', 'wb') as arquivo:
#     pickle.dump([], arquivo)

def menu():
    print('1 - Inserir produto')
    print('2 - Listar produtos')
    print('3 - Remover produto')
    print('4 - Sair')
    opc = int(input('Opção: '))
    return opc

def extrairDados():
    with open('prova_b2.1_barbosa/compras.dat', 'rb') as arquivo: # pegar os dadoss ja coisados
        dados = pickle.load(arquivo)
    return dados

def salvarDados(dados_atualizados):
    with open('prova_b2.1_barbosa/compras.dat', 'wb') as arquivo: # salvar os novos dadoos atualizdos
        pickle.dump(dados_atualizados, arquivo)

def cadastrarProduto(dados):
    print('INSERIR')
    nome = str(input('Informe o nome do produto: ')).strip()
    
    # verificar se o produt ja foi esta cadastrado
    cadastrado = False
    for registro in dados:
        if nome == registro['nome']:
            cadastrado = True
            
    if cadastrado:
        print('Já existe um item cadastrado com esse nome')
        
    else:
        valor = float(input('Informe o valor unitário (R$): '))
        quantidade = int(input('Informe a quantidade: '))
        
        # print(type(dados))
        dados.append({
            "nome": nome,
            "valor": valor,
            "quantidade": quantidade
        })
        
        salvarDados(dados)
        print('Produto cadastrado com sucesso!')

def imprimirSaida(dados):
    print('LISTAR')
    total = 0
    # oh fuck man, eu tenho que voltar aq ddispoisi
    for registro in dados:
        print(f'{registro['nome']} {registro['quantidade']} x R$ {registro['valor']:.2f} = R$ {(registro['quantidade']*registro['valor']):.2f}')
        total += (registro['quantidade']*registro['valor'])
    print(f'Total: R$ {total:.2f}')

def removerItem(dados):
    print('REMOVER')
    nome = str(input('Nome do produto cadastrado: ')).strip()
    cadastrado = False # verificad se o produtofodasse ta cadastado
    for chave, registro in enumerate(dados): # vou precisar o índice para remover o elemento da lista, mas não pode na iteração do for, então tenho que crair uam variavel para armazenar
        if registro['nome'] == nome:
            item = chave
            cadastrado = True
    
    if cadastrado:
        print('Produto removido com sucesso!')
        dados.pop(item)
        salvarDados(dados)
    else:
        print('Produto não encontrado!')

def main():
    while True:
        opc = menu()
        dados = extrairDados()
        match opc:
            case 1:
                cadastrarProduto(dados)
                
            case 2:
                imprimirSaida(dados)
                
            case 3:
                removerItem(dados)
            
            case 4:
                print('Saindo do programa...')
                break
            case _:
                print('Opção Invalida!')
                
if __name__ == '__main__':
    main()