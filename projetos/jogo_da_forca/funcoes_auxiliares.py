import os

def gerarCampoPalavra(palavra_secreta):
    lista_decifradora = []
    for _ in range(len(palavra_secreta)):
        lista_decifradora.append('_')
    
    return lista_decifradora

def exibirCaracteresAcertados(lista_decifradora):
    for elementos in lista_decifradora:
        print(elementos, end= ' ')
    print()

def limparTerminal():
    os.system('cls')

# def verificaCaractere(letra, palavra_secreta, lista_decifradora,  n_letras_presentes = 0):
#     for index_lista in range(len(palavra_secreta)):
#         if palavra_secreta[index_lista] == letra:
#             lista_decifradora[index_lista] = letra
#             n_letras_presentes += 1
        
#         return n_letras_presentes, 
    

