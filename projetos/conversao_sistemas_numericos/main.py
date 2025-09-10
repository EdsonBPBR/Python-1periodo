# octal -> hexadecimal : octal -> decimal e decimal -> hexadecimal
# hexadecimal -> octal : hexadecimal -> decimal e decimal -> octal
# hexadecimal -> binario : hexadecimal -> decimal e decimal -> binario
# binario -> hexadecimal : binario -> decimal e decimal -> hexadecimal
# binario -> octal : binario -> decimal e decimal -> octal
# octal -> binario : octal -> decimal e decimal -> binario
# octal -> hexadecimal > octal -> decimal e decimal -> hexadecimal
from decimal_para_binario import decimalBinario
import os

if __name__ == '__main__':
    while True:
        print('"0" - SAIR')
        print('"1" - DECIMAL PARA BINARIO')
        print('"2" - OCTAL PARA BINARIO')
        
        opcao = int(input())
        os.system('cls')
        
        if opcao == 0:
            print('Saindo do programa...')
            break
            
        elif opcao == 1:
            decimal = int(input('Decimal: '))
            print(decimalBinario(decimal))
            
            print('Pressione ENTER para continuar...')
            input()
            os.system('cls')
            
        elif opcao == 2:
            pass
        
        else:
            print('Opção inválida!')