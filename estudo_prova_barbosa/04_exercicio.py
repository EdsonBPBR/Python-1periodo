def contaBuracos(texto):
    buracos = {
        'A': 1,
        'D': 1,
        'O': 1,
        'P': 1,
        'R': 1,
        'B': 2,
    }
    
    total_buracos = 0
    for caractere in texto:
        if caractere in buracos:
            total_buracos += buracos[caractere]
    return total_buracos
    
def main():
    texto = str(input("Informe um texto: ")).strip().upper()
    print(f"'{texto}' possuí {contaBuracos(texto)} buracos")
    
if __name__ == '__main__':
    main()