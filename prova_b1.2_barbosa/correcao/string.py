def menu():
    print('1) Fornecer texto')
    print('2) Substituir caractere')
    print('3) Procurar caractere')
    print('4) Inverter texto')
    print('5) Verificar se é palíndromo')
    print('6) Sair')
    
def fornecerTexto():
    texto = input("Informe um texto: ").strip()
    return texto
    
def substituiCaractere(texto, caractere_presente):
    novo_caractere = input(f"Informe o novo caractere que deseja substuir por '{caractere_presente}': ")
    texto = texto.replace(caractere_presente, novo_caractere)
    return (texto)
    
def buscarCaractere(texto):
    buscar_caractere = input("Informe o caractere que deseja buscar: ")
    if buscar_caractere in texto:
        return f"'{buscar_caractere}' está presente no texto informado"
    else:
        return f"'{buscar_caractere}' NÃO está presente no texto informado"
    
def inverterTexto(texto):
    
    texto = texto[::-1]
    return texto
    
def verificaPalindromo(texto):
    if texto == texto[::-1]:
        return (f"'{texto}' é um palíndromo")
    else:
        return (f"'{texto}' NÃO é um palíndromo")

def main():
    while True:
        menu()
        opc = int(input("Opção: "))
        
        match opc:
            case 1:
                texto = fornecerTexto()
                
            case 2:
                caractere_presente = input("Informe o caractere que deseja substituir: ").strip()
                if caractere_presente in texto:
                    texto = substituiCaractere(texto, caractere_presente)
                    print(texto)
                else:
                    print('Esse caractere não está presente no texto. Obs: o sistema diferencia caracteres Maiusculos e Minusculos')
                    
            case 3:
                print(buscarCaractere(texto))
                    
            case 4:
                texto = inverterTexto(texto)
                print(texto)
            
            case 5:
                print(verificaPalindromo(texto))
                    
            case 6:
                print('Saindo do programa...')
                break
            case _:
                print('Opção inválida!')
                
if __name__ == '__main__':
    main()