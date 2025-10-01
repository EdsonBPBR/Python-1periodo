def calculaSomatorio(linha):
    somatorio = 0
    
    for n in range(12):
        entrada_linha = str(input()).split()
        
        if n == linha:
            for elementos in range(len(entrada_linha)):
                somatorio += int(entrada_linha[elementos])
    return somatorio
        
if __name__ == '__main__':
    linha = int(input())
    operacao = str(input()).upper()
    somatorio = calculaSomatorio(linha)

    if operacao == 'M':
        media = somatorio / 12
        print(f'{media:.1f}')
    elif operacao == 'S':
        print(f'{somatorio:.1f}')
# somatorio = 0

# for n in range(12):
#     entrada_linha = str(input()).split()
    
#     if n == linha:
#         for elementos in range(len(entrada_linha)):
#             somatorio += int(entrada_linha[elementos])
