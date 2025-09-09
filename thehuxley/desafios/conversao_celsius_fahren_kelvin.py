# Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo usuário para as outras escalas de medida.
#  Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
#  Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
#  Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius
#K = C + 273,15
# C / 5 = F - 32 / 9

def conversorTemperaturas(escala, temperatura):
    if escala == 'C' and temperatura >= -273.15:
        f = 1.8 * temperatura + 32
        k = temperatura + 273.15
        print(f'{f:.2f} F')
        print(f'{k:.2f} K')

    elif escala == 'F' and temperatura >= -459.67:
        c = (5 * temperatura - 160) / 9
        k = c + 273.15
        print(f'{c:.2f} C')
        print(f'{k:.2f} K')

    elif escala == 'K' and temperatura >= 0:
        c = temperatura - 273.15
        f = 1.8 * c + 32
        print(f'{c:.2f} C')
        print(f'{f:.2f} F')

    else:
        print('Valor de temperatura abaixo do minimo')
 
 
if __name__ == '__main__':        
    escala = str(input()).upper()
    temperatura = float(input())
    conversorTemperaturas(escala, temperatura)

