def menu():
    print('1 - CADASTRAR')
    print('2 - REMOVER')
    print('3 - VISUALIZAR')
    
def extrairDados():
    with open('exercicios_slide14/arquivos/registros_pessoas.txt', 'r') as arquivo:
        extrair_dados = arquivo.readlines()
    return extrair_dados

def cadastrarRegistro():
    pass


while True:
    menu()
    opc = int(input(": "))
    match opc:
        case 1:
            id = 0
            extrair_dados = extrairDados()
            for linha in extrair_dados: # inserir pois não dava certo pegar o ID por particionadores, se fosse 10 eie iria pegar 1
                id += 1 # esse mecanismo de ID necessita ser melhorado! prioridade: alta, eu posso colocar no arquivo tbm em qual ID parou, para não acontecer repetições
    
            nome = str(input('Nome: ')).upper()
            idade = int(input('Idade: '))
                       
            novo_registro = f'{id} {nome} {idade}\n'
            extrair_dados.append(novo_registro)

            with open('exercicios_slide14/arquivos/registros_pessoas.txt', 'w') as arquivo:
                for registros in extrair_dados: # salva as alterações no arquivo, sobrescrevendo
                    arquivo.write(registros)
        case 2:
            id_registro = str(input("ID: "))
        
            extrair_dados = extrairDados()
            freq = False
            for linha in extrair_dados: # inserir pois não dava certo pegar o ID por particionadores, se fosse 10 eie iria pegar 1
                tupla = linha.split()
                
                if id_registro in tupla[0]: # verifica se o registro existe
                    print(tupla)
                    freq = True
                    
            if not(freq):
                print('Usuário não encontrado!')   
            else:
                with open('exercicios_slide14/arquivos/registros_pessoas.txt', 'w') as arquivo:
                    for posicao, linha in enumerate(extrair_dados):
                        if posicao == int(id_registro):
                            pass
                        else:
                            arquivo.write(linha)
        case 3:
            # melhorar depois inserindo os elementos em uma tabela
            with open('exercicios_slide14/arquivos/registros_pessoas.txt', 'r') as arquivo:
                extrair_dados = arquivo.read()
            print(extrair_dados)
        case _:
            print('Opção Inválida!')