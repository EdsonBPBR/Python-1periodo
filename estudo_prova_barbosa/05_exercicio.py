# 10 fileiras (A, B, ..., I, J)
# 20 poltronas (1, 2, ...,19, 20)
import os
def menu():
    print('1 - RESERVAR POLTRONA')
    print('2 - VISUALIZAR POLTRONAS')
    print('3 - SAIR')

def comprarPoutrona():
    fileira = str(input("Informe a fileira (A-J): ")).upper()
    if fileira in 'ABCDEFGHIJ':
        n_poutrona = int(input("Informe o nº poutrona: "))

        if 1 <= n_poutrona <= 20:
            registro = (fileira, n_poutrona) 
            if registro in poutronas_reservadas:
                print('Poutrona já reservada! Tente selecionar outra')
                
            else:
                print(f'Poutrona {fileira}{n_poutrona} disponível!')
                confirmacao = str(input('Deseja confirmar a compra? S-sim, N-não: ')).strip().upper()

                if confirmacao == 'S':
                    poutronas_reservadas.add(registro)
                    print(f'Poutrona {fileira}{n_poutrona} comprada com sucesso!')
                    
                elif confirmacao == 'N':
                    print('Pedido Cancelado...')
                
                else:
                    while confirmacao != 'N' or confirmacao != 'S':
                        confirmacao = str(input('Deseja confirmar a compra? S-sim, N-não: ')).strip().upper()
                        
                        if confirmacao == 'S':
                            poutronas_reservadas.add(registro)
                            print(f'Poutrona {fileira}{n_poutrona} comprada com sucesso!')
                            break
                        
                        elif confirmacao == 'N':
                            print('Pedido cancelado...')
                            break           
        else:
            print('Poutrona inválida!')
    else:
        print('Fileira inválida! Somente no invervalo de (A-J)')

poutronas_reservadas = set()
os.system('cls')
while True:
    menu()
    opc = int(input('Opção: '))
    match opc:
        case 1:
            comprarPoutrona()
            
        case 2:
            print(poutronas_reservadas)
            
        case 3:
            print('Saindo do programa...')
            break    
        
        case _:
            print('Opção Inválida!')