def menu():
    print('1 - CADASTRAR FUNCIONARIO')
    print('2 - OBTER RESULTADO E RECALCULAR SALÁRIOS')
    print('3 - SAIR')
    opc = int(input(': '))
    return opc
   
def cadastrarFuncionario(registros):
    nome = str(input('Nome: '))
    salario_atual = float(input('Salário (R$): '))
    dado = (nome, salario_atual)
    registros.append(dado)
    
def calculaSalario(registro):
    if registro[1] > 5000:
        novo_salario = registro[1] * 1.05
    elif registro[1] >= 2000 and registro[1] <= 5000:
        novo_salario = registro[1] * 1.15
    else:
        novo_salario = registro[1] * 1.2
    return novo_salario
    
def imprimeResultados(registros):
    total_novos_salarios = 0
    total_salarios_antigos = 0
    funci_menores = []
    
    print('Reajustes: ')
    for registro in registros:
        total_salarios_antigos += registro[1]
        novo_salario = calculaSalario(registro)
        
        if novo_salario < 2000:
            funci_menores.append(registro[0])
        total_novos_salarios += novo_salario
        print(registro[0], novo_salario)
        
        print(f'Aumento de: R$ {total_novos_salarios-total_salarios_antigos:.2f}')
        print('Funcionários com salários menores que R$ 2.000,00: ')
        for funcionario in funci_menores:
            print(funcionario)
    
def main():
    registros = []
    while True:
        try:
            opc = menu()
            match opc:
                case 1:
                    cadastrarFuncionario(registros)
                    
                case 2:
                    imprimeResultados(registros)
                    
                case 3:
                    print('Saindo do programa...')
                    break
                
                case _:
                    print('Opção Inválida!')
        except ValueError:
            print('Dado de entrada inválido!')
            
if __name__ == '__main__':
    main()