# Reescreva o programa (Menu para 4 opera ̧c ̃oes - Aula sobre while) de modo que
# ap ́os selecionar a op ̧c ̃ao no menu a tela seja limpa e ent ̃ao os dados sejam
# solicitados e o resultado exibido. Ap ́os exibir o resultado da opera ̧c ̃ao desejada deve
# ser exibida a mensagem “Pressione ENTER para continuar...”. A tela ser ́a limpa
# novamente e o usu ́ario ent ̃ao retornar ́a ao menu principal.
from funcoes_4_operacoes import * #chamando a biblioteca que criei
#from colored import fore, back, style #aplicar isso daqui
#função doctest


# main
if __name__ == "__main__":
    while True:
        limpar_terminal()
        
        opcao = menu()
        
        limpar_terminal()
        
        if opcao == 0:
            print(f'Saindo do programa...')
            break
        
        elif opcao == 1:
            print('SOMA')
            valor_1 = float(input('Informe um valor: '))
            valor_2 = float(input('Informe outro valor: '))
            print(soma(valor_1, valor_2))
            
            print('Pressione ENTER para continuar...')
            input()
        
        elif opcao == 2:
            print('SUBTRAÇÃO')
            valor_1 = float(input('Informe um valor: '))
            valor_2 = float(input('Informe outro valor: '))
            print(subtracao(valor_1, valor_2))
            
            print('Pressione ENTER para continuar...')
            input()
        
        elif opcao == 3:
            print('DIVISÃO')
            valor_1 = float(input('Informe um valor: '))
            valor_2 = float(input('Informe outro valor: '))
            print(divisao(valor_1, valor_2))
            
            print('Pressione ENTER para continuar...')
            input()
        
        elif opcao == 4:
            print('MULTIPLICAÇÃO')
            valor_1 = float(input('Informe um valor: '))
            valor_2 = float(input('Informe outro valor: '))
            print(multiplicacao(valor_1, valor_2))
            
            print('Pressione ENTER para continuar...')
            input()
        
        else:
            print('Opção Inválida! Tente novamente!')
            
            print('Pressione ENTER para continuar...')
            input()