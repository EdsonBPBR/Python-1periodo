# (M ́edia de alunos) Crie um programa em Python para calcular a m ́edia de duas
# notas um conjunto de alunos. Caso o valor -1 seja informado o programa deve
# finalizar sua execu ̧c ̃ao
from funcoes_media_alunos_melhorias import *

if __name__ == '__main__':
    c = 1
    cor_normal, cor_1, cor_2 = coresTerminal()
    
    while True:
        menu()
        opcao = int(input())
        limparTerminal() 
        
        if opcao == 1:
            n1 = float(input(f'Informe a nota AB1 do aluno {c}: '))
            n2 = float(input(f'Informe a nota AB2 do aluno {c}: '))

            print(f'A média do aluno {c} é {calculaMedia(n1, n2)}')
            
            print('Pressione ENTER para continuar...')
            input()
            limparTerminal()
            
            c += 1
        
        elif opcao == 2:
            limparTerminal()
            print(f'{cor_1} Saindo do programa...')
            print(f'{cor_normal}')
            break
        
        else:
            print('Entrada inválida!')
        