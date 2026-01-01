texto = str(input()).strip()
escolha = str(input()).strip()

def busca():
    freq = 0
    for caractere in texto:
        if escolha == caractere:
            freq += 1
    return freq
            
if busca() > 0:
    print(f'O caractere buscado ocorre {busca()} vezes na sequencia.')
else:
    print('Caractere nao encontrado.')