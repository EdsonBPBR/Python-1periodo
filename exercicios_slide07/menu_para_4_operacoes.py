# (Menu para 4 opera ̧c ̃oes) Crie um programa em Python para exibir os resultados das
# quatro opera ̧c ̃oes para dois valores fornecidos pelo usu ́ario. Deve ser exibido o
# resultado de uma opera ̧c ̃ao por vez, de acordo com uma escolha do usu ́ario a partir
# de um menu. O programa deve retornar ao menu ap ́os exibir o resultado da
# opera ̧c ̃ao selecionada, deve ser apresentada uma op ̧c ̃ao para finalizar o programa.

while True:
    print('1) Soma')
    print('2) Subtração')
    print('3) Divisão')
    print('4) Multiplicação')
    print('0) Sair')

    opcao = int(input('Informe uma das opções acima: '))

    if opcao == 0:
        print('Saindo do programa...')
        break
    
    elif opcao == 1:
        valor_1 = float(input('Informe um valor: ')) #cabe o conceito de funções, pois há repetição de códigos
        valor_2 = float(input('Informe outro valor: '))
        resultado = valor_1 + valor_2
        print(f'{valor_1} + {valor_2} = {resultado}')
    
    elif opcao == 2:
        valor_1 = float(input('Informe um valor: '))
        valor_2 = float(input('Informe outro valor: '))
        resultado = valor_1 - valor_2
        print(f'{valor_1} - {valor_2} = {resultado}')
    
    elif opcao == 3:
        valor_1 = float(input('Informe um valor: '))
        valor_2 = float(input('Informe outro valor: '))
        resultado = valor_1 / valor_2
        print(f'{valor_1} / {valor_2} = {resultado}')
    
    elif opcao == 4:
        valor_1 = float(input('Informe um valor: '))
        valor_2 = float(input('Informe outro valor: '))
        resultado = valor_1 * valor_2
        print(f'{valor_1} x {valor_2} = {resultado}')
    
    else:
        print('Opção Inválida! Tente novamente!')