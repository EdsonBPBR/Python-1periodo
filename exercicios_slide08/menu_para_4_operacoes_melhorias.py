# Reescreva o programa (Menu para 4 opera ̧c ̃oes - Aula sobre while) de modo que
# ap ́os selecionar a op ̧c ̃ao no menu a tela seja limpa e ent ̃ao os dados sejam
# solicitados e o resultado exibido. Ap ́os exibir o resultado da opera ̧c ̃ao desejada deve
# ser exibida a mensagem “Pressione ENTER para continuar...”. A tela ser ́a limpa
# novamente e o usu ́ario ent ̃ao retornar ́a ao menu principal.
import os

while True:
    os.system('cls')
    
    print('1) Soma')
    print('2) Subtração')
    print('3) Divisão')
    print('4) Multiplicação')
    print('0) Sair')

    opcao = int(input('Informe uma das opções acima: '))
    os.system("cls")
    
    if opcao == 0:
        print('Saindo do programa...')
        break
    
    elif opcao == 1:
        print('SOMA')
        valor_1 = float(input('Informe um valor: ')) #cabe o conceito de funções, pois há repetição de códigos
        valor_2 = float(input('Informe outro valor: '))
        resultado = valor_1 + valor_2
        print(f'{valor_1} + {valor_2} = {resultado}')
        
        print('Pressione ENTER para continuar...')
        input()
    
    elif opcao == 2:
        print('SUBTRAÇÃO')
        valor_1 = float(input('Informe um valor: '))
        valor_2 = float(input('Informe outro valor: '))
        resultado = valor_1 - valor_2
        print(f'{valor_1} - {valor_2} = {resultado}')
        
        print('Pressione ENTER para continuar...')
        input()
    
    elif opcao == 3:
        print('DIVISÃO')
        valor_1 = float(input('Informe um valor: '))
        valor_2 = float(input('Informe outro valor: '))
        resultado = valor_1 / valor_2
        print(f'{valor_1} / {valor_2} = {resultado}')
        
        print('Pressione ENTER para continuar...')
        input()
    
    elif opcao == 4:
        print('MULTIPLICAÇÃO')
        valor_1 = float(input('Informe um valor: '))
        valor_2 = float(input('Informe outro valor: '))
        resultado = valor_1 * valor_2
        print(f'{valor_1} x {valor_2} = {resultado}')
        
        print('Pressione ENTER para continuar...')
        input()
    
    else:
        print('Opção Inválida! Tente novamente!')
        
        print('Pressione ENTER para continuar...')
        input()