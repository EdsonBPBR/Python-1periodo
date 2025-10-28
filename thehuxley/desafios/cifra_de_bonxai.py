# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# M - > R
# A
alfa = 'abcdefghijklmnopqrstuvwxyz'

def codigoCesar(texto, chave):
    texto_criptografado = ''
    for caractere in texto:
        texto_criptografado += f'{alfa[(alfa.index(caractere)+chave)%26]}'

    return texto_criptografado

def main():
    tamanho_texto = int(input())
    texto = input().strip()
    chave = int(input())
    print(codigoCesar(texto, chave))

if __name__ == '__main__':
    main()