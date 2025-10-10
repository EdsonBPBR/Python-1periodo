# em sua sala de proje ̧c ̃ao existem 10 fileiras de poltronas, identificadas por letras e
# em cada fileira existem 20 poltronas, identificadas por valores inteiros.
import os
import random

def menu():
    print('1 - ALOCAR POLTRONA')
    print('2 - REALOCAR POLTRONA')
    print('3 - VISUALIZAR')
    print('0 - SAIR')

def locarPoutrona():
    os.system('cls')
    fileiras_disponiveis = 'ABCDEFGHIJ'
    
    fileira = str(input("Fileira (A-J): ")).upper()
    if fileira in fileiras_disponiveis:
        cadeira = int(input("Cadeira (1-20): "))
                
        if cadeira >= 1 and cadeira <= 20:
                        
            if (fileira, cadeira) in alocadas:
                print('Poutrona já locada!')
            else:
                while True:
                    confirmar = str(input(f"Deseja confirmar a locação em {fileira}{cadeira}? SIM | NAO : ")).upper()
                                
                    if confirmar == 'SIM':
                        alocadas.append((fileira, cadeira))
                        
                        print(f'Poutrona {fileira}{cadeira} alocada com sucesso! Gerando QRCode... \n')
                        break
                                
                    elif confirmar == 'NAO':
                        print('Operação Cancelada!')
                        break
                                
                    else:
                        print('Entrada Inválida!')
        else:
            print('Cadeiras vão de 1 a 20! \n')
    else:
        print('Fileiras vão de A a J! \n')               
    input("Pressione ENTER para continuar \n")
            
alocadas = []
chaves = set()

if __name__ == '__main__':
    while True:
        os.system('cls')
        menu()
        
        try:
            opc = int(input(": "))
            
            if opc == 0:
                print('Saindo do programa...')
                break
            
            elif opc == 1:
                locarPoutrona()
            
            elif opc == 2:
                pass

            elif opc == 3:
                for posicao in range(len(alocadas)):
                    print(alocadas[posicao])
                input("Pressione ENTER para continuar \n")
            
            else:
                print('Opção Inválida! Tente novamente.')
        
        except ValueError:
            print('Entrada da Opção Inválida! Somente números inteiros! \n')
            input("Pressione ENTER para continuar \n")