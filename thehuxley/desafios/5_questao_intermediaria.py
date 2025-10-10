if __name__ == '__main__':
    registros = {}

    while True:
        nome = str(input("Nome aluno: "))
        if nome == 'sair':
            break
        
        nota = float(input("Nota aluno: "))
        registros[nome] = nota
        
    print(registros)