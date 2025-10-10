# 3️⃣ Questão Intermediária+ – Manipulação de Strings
# Peça uma frase ao usuário e mostre:
# Quantas palavras ela tem,
# Quantas vogais existem na frase.

if __name__ == '__main__':
    frase = str(input("Digite uma frase: ")).upper()

    analise = list(frase)
    vogais = 'AEIOUÉ'

    n_vogais = 0
    for caractere in analise:
        if caractere in vogais:
            n_vogais += 1
            
    print(f'Palavras: {len(frase.split())}')
    print(f'Vogais: {n_vogais}')