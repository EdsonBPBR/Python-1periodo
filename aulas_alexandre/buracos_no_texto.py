#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
def contaBuracos(texto, caracteres_um = ['A', 'D', 'O', 'P', 'Q', 'R']):
    n_buracos = 0
    
    for elemento in texto:
        if elemento in caracteres_um:
            n_buracos += 1

        elif elemento == "B":
            n_buracos += 2

        else:
            n_buracos += 0
    
    return n_buracos

if __name__ == '__main__':
    c = 0
    n = int(input())
    while c < n:
        texto = str(input()).upper()
                
        print(contaBuracos(texto))
        c += 1