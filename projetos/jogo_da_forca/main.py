from palavras_secretas import escolhePalavra
from estagios_boneco_forca import estagiosForca
from funcoes_auxiliares import gerarCampoPalavra, exibirCaracteresAcertados, limparTerminal

if __name__ == '__main__':
    palavra_secreta = list(escolhePalavra())
    lista_decifradora = gerarCampoPalavra(palavra_secreta)
    tentativas = 0

    while True:
        if lista_decifradora == palavra_secreta:
            exibirCaracteresAcertados(lista_decifradora)
            print('Parabéns! Você ganhou!')
            break
            
        elif tentativas > 5:
            print('Você MORREU!')
            print(f'A palavra correta era: {escolhePalavra()}')
            break   
        
        elif tentativas == 0:
            limparTerminal()
            print(estagiosForca(tentativas))
            
        exibirCaracteresAcertados(lista_decifradora)
        
        letra = str(input('Informe uma LETRA ou PALAVRA COMPLETA: ')).upper()
        #ainda falta implementar diversos requisitos, entre eles: quais caracteres já foram inseridos, palavra completa e formatação aprimorada
        
        n_letras_presentes = 0
        for index_lista in range(len(palavra_secreta)):
            if palavra_secreta[index_lista] == letra:
                lista_decifradora[index_lista] = letra
                n_letras_presentes += 1
        
        if n_letras_presentes > 0:
            print(estagiosForca(tentativas))
            pass
    
        else:
            limparTerminal()
            tentativas += 1
            print(estagiosForca(tentativas))
            
                
                
    