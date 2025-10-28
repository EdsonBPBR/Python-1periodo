import pickle

disciplina = []
controle_matriculas = set()

with open('exercicios_slide11/disciplina.txt', 'wb') as arquivo:
    pickle.dump([], arquivo)

def carregarDados():
    global disciplina
    global controle_matriculas
    with open('exercicios_slide11/disciplina.txt', 'rb') as arquivo:
        disciplina = pickle.load(arquivo)
        controle_matriculas = pickle.load(arquivo)

def gravarDados():
    with open('exercicios_slide11/disciplina.txt', 'wb') as arquivo:
        pickle.dump(disciplina, arquivo)
        pickle.dump(controle_matriculas, arquivo)

def criarDiscente(nome, matricula):
    if matricula in controle_matriculas:
        print('Matrícula já existente!') 
    
    else:
        discente = (nome, matricula)
        disciplina.append(discente)
        controle_matriculas.add(matricula)
        print('Discente cadastrado com sucesso!')
    
def listarDiscente():
    for discente in disciplina:
        print(f'Matricula: {discente[1]} Matricula: {discente[0]}')

def menu():
    print('1 - Cadastrar Discente')
    print('2 - Listar Discentes Cadastrados')
    print('0 - Sair')
    opc = int(input(": "))
    return opc

carregarDados()
while True:
    opc = menu()
    match opc:
        case 0:
            gravarDados()
            break
        
        case 1:
            nome = str(input('Nome: '))
            matricula = str(input('Matricula: '))
            criarDiscente(nome, matricula)

        case 2:
            listarDiscente()
            input('Pressione ENTER para continuar\n')
        
        case _:
            print('Opção Inválida!')