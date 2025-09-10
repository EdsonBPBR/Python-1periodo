# octal -> hexadecimal : octal -> decimal e decimal -> hexadecimal
# hexadecimal -> octal : hexadecimal -> decimal e decimal -> octal
# hexadecimal -> binario : hexadecimal -> decimal e decimal -> binario
# binario -> hexadecimal : binario -> decimal e decimal -> hexadecimal
# binario -> octal : binario -> decimal e decimal -> octal
# octal -> binario : octal -> decimal e decimal -> binario
# octal -> hexadecimal > octal -> decimal e decimal -> hexadecimal
from decimal_para_binario import decimalBinario
from octal_para_decimal import octalDecimal
from hexadecimal_para_decimal import hexadecimalDecimal
from decimal_para_octal import decimalOctal
from binario_para_decimal import binarioDecimal
from decimal_para_hexadecimal import decimalHexadecimal
from funcoes_auxiliares import *


if __name__ == '__main__':
    while True:
        limparTerminal()
        menu()
        
        opcao = int(input(': '))
        limparTerminal()
        
        if opcao == 0:
            print('Saindo do programa...')
            break
            
        elif opcao == 1:
            print('1 - DECIMAL PARA BINÁRIO')
            print('Informe o número em DECIMAL: ')
            decimal = int(input())
            
            saidaPersonalizada(
                decimalBinario(decimal)
                )
            continuarOperacao()
            
        elif opcao == 2:
            print('2 - OCTAL PARA BINÁRIO')
            print('Informe o número em OCTAL:')
            octal = str(input())
            
            saidaPersonalizada(
                decimalBinario(
                    octalDecimal((octal)
                        )
                    )
                )
            
            continuarOperacao()
        
        elif opcao == 3:
            print('3 - HEXADECIMAL PARA BINÁRIO')
            print('Informe o número em HEXADECIMAL:')
            hexadecimal = str(input())
        
            saidaPersonalizada(
                decimalBinario(
                    hexadecimalDecimal(hexadecimal)
                    )
                )
            
            continuarOperacao()
        
        elif opcao == 4:
            print('4 - DECIMAL PARA OCTAL')
            print('Informe o número em DECIMAL:')
            decimal = int(input())
            
            saidaPersonalizada(
                decimalOctal(decimal)
                )
            
            continuarOperacao()
            
        elif opcao == 5:
            print('5 - BINÁRIO PARA OCTAL') 
            print('Informe o número em BINÁRIO:')
            binario = str(input())
            
            saidaPersonalizada(
                decimalOctal(
                    binarioDecimal(binario)
                    )
                )

            continuarOperacao()
            
        elif opcao == 6:
            print('6 - HEXADECIMAL PARA OCTAL')
            print('Informe o número em HEXADECIMAL:')
            hexadecimal = str(input())

            saidaPersonalizada(
                decimalOctal(
                    hexadecimalDecimal(hexadecimal)
                    )
                )            
            
            continuarOperacao()
            
        elif opcao == 7:
            print('7 - DECIMAL PARA HEXADECIMAL')
            print('Informe o número em DECIMAL:')
            decimal = int(input())
            
            saidaPersonalizada(
                decimalHexadecimal(decimal)
                )

            continuarOperacao()
        
        elif opcao == 8:
            print('8 - OCTAL PARA HEXADECIMAL')
            print('Informe o número em OCTAL:')
            octal = str(input())
            
            saidaPersonalizada(
                decimalHexadecimal(
                    octalDecimal(octal)
                    )
                )
            
            continuarOperacao()
        
        elif opcao == 9:
            print('9 - BINÁRIO PARA HEXADECIMAL')
            print('Informe o número em BINÁRIO:')
            binario = str(input())
            
            saidaPersonalizada(
                decimalHexadecimal(
                    binarioDecimal(binario)
                    )
                )
            
            continuarOperacao()
        
        else:
            print('Opção inválida!')
            continuarOperacao()