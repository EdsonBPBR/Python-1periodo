# conversão de um número decimal para um número octal

# tem como entrada numero inteiro, somente
def decimalOctal(decimal):
    octal = []
    string_octal = ''
    
    resultado = decimal
    while True:
        octal.append(resultado % 8)
        resultado = resultado // 8
        
        if resultado == 0:
            break
        
    octal.reverse()

    for elemento in octal:
        string_octal += f'{elemento}'

    return string_octal



    
    