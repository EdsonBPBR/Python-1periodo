# Implemente um sistema que gerencie funcionários de uma empresa, oferecendo as seguintes funcionalidades:
# 1. Adicionar funcionário: Cadastrar um funcionário com nome e salário.
# 2. Exibir funcionários: Mostrar a lista completa de funcionários com seus respectivos salários.
# 3. Remover funcionário: Permitir a exclusão de um funcionário pelo nome.
# 4. Alterar salário: Permitir que o salário de um funcionário seja atualizado.
# 0. Encerrar programa: Finalizar o sistema liberando todos os recursos alocados dinamicamente.

# O ALGORITMO RESOLVE O PROBLEMA, NO ENTANTO, TEM UM, SOMENTE UM, PASSO DA SUBMISSÃO QUE NÃO ESTÁ DANDO CERTO E EU NÃO SEI O POR QUÊ.

registros = {}
while True:
    opc = int(input())
    
    if opc == 0:
        break
    
    elif opc == 1:
        nome = str(input())
        salario = float(input())
        registros[nome] = [salario] 

    elif opc == 2:
        funcionarios = list(registros.keys())
        for i in range(len(funcionarios)):
            print(f'{i+1}. {funcionarios[i]}')
            print(f'{registros[funcionarios[i]][0]:.2f}')
        print()
        
    elif opc == 3:
        nome = str(input())
        
        if nome in registros:
            registros.pop(nome)
        else:
            print('Funcionario nao encontrado.')
    
    elif opc == 4:
        nome = str(input())
        
        if nome in registros:
            novo_salario = float(input())
            registros[nome][0] = novo_salario
        else:
            print('Funcionario nao encontrado.')

    else:
        print('Opcao invalida')