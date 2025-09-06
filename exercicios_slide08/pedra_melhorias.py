#teroura corta papel
#papel cobre pedra
#pedra esmaga largato ---------
#largato envenena spock  ---------
#spock derrete tesoura ---------
#tesoura decapita largato ---------
#largato come papel ------
#papel refuta spock
#spock vaporiza pedra
#pedra quebra tesoura

#iniciei fazendo o pedra papel tesoura normal:
from funcoes_pedra_papel_smoke import menu, limpar_tela, verifica_vencedor, escolha_computador

if __name__ == '__main__':
    while True:
        jogador1 = menu()
        jogador2 = escolha_computador()

        limpar_tela()
            
        print(escolha_computador())

        if jogador1 == 0:
            print('SAINDO... ')
            break
        else:
            print(verifica_vencedor(jogador1, jogador2))
        
        input("Pressione ENTER para continuar...")
        limpar_tela()