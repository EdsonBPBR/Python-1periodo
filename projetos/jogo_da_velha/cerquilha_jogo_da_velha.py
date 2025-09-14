import os
def limparTerminal():
   os.system('cls')         
# print(f"""
#         ||        ||
#         ||        ||
#         ||        ||
# ========||========||========
#         ||        ||
#         ||        ||
#         ||        ||
# ========||========||========
#         ||        ||
#         ||        ||
#         ||        ||
      
#       """)


# jogada = str(input())
# posicoes.insert(posicoes.index(f'{jogada}'), 'X')

# c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 'X  '

posicoes = {
    'C1':'   ',    
    'C2':'   ',   
    'C3':'   ',   
    'C4':'   ',   
    'C5':'   ',   
    'C6':'   ',   
    'C7':'   ',   
    'C8':'   ',   
    'C9':'   ',   
}

limparTerminal()

#menu e placar
print('='*51)
print(f'{'MENU': ^51}')
print('='*51)
print(f'{'JOGADOR 1 = X': ^24}| {'JOGADOR 2 = O': ^24}')
freq_jogador = 0

while True:
    if freq_jogador % 2 == 0:
        identificao_jogador = 'Jogador 1 - "X"'
    else:
        identificao_jogador = 'Jogador 2 - "O"'
    print(f"""
            ||        ||
       {posicoes['C1']}  ||   {posicoes['C2']}  ||   {posicoes['C3']}
            ||        ||
    ========||========||========
            ||        ||
       {posicoes['C4']}  ||   {posicoes['C5']}  ||   {posicoes['C6']}
            ||        ||
    ========||========||========
            ||        ||
       {posicoes['C7']}  ||   {posicoes['C8']}  ||   {posicoes['C9']}
            ||        ||
        """)
    
    entrada = str(input(f'{identificao_jogador}, informe a Posição da jogada: ')).upper() #jogada X
    
    # tratamento da entrada   
    
    
    # interação com o dicionário:
    if posicoes[entrada] == '   ':
        if freq_jogador % 2 == 0:
            posicoes[entrada] = 'X  '
        else:
            posicoes[entrada] = 'O  '
        print(posicoes[entrada])
        
        limparTerminal()
        freq_jogador += 1
    else:
        limparTerminal()
        print('Já está ocupado! Tente novamente em outra posição')
        

    
    