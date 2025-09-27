# Construa um código que calcula a área e o volume de um corpo sólido com base nas entradas do programa. 
# Adote pi = 3.1415
pi = 3.1415

def verificaForma(opc_forma):
    if opc_forma == 'c':
        status = 'C'
    elif opc_forma == 'e':
        status = 'E'
    else:
        status = "Entrada invalida! Voce deve usar 'c' (cilindro) ou 'e' (esfera)."

    return status

def areaCilindro(raio, altura):
    calculo = (2 * pi * raio) * ((raio + altura))

    return calculo

def volumeCilindro(raio, altura):
    calculo = pi * (raio**2) * altura

    return calculo

def areaEsfera(raio):
    calculo = 4 * pi * (raio**2)
    
    return calculo

def volumeEsfera(raio):
    calculo = (4*pi*(raio**3)) / 3

    return calculo

if __name__ == '__main__':
    opc_forma = str(input())
    
    if opc_forma == 'c' or opc_forma == 'e':

        status = verificaForma(opc_forma)
        opc_calculo = str(input())

        if opc_calculo == 'a' or opc_calculo == 'v':
            if status == 'C' and opc_calculo == 'a':
                raio = float(input())
                altura = float(input())

                print(f'A area do cilindro de raio {raio:.2f} e altura {altura:.2f} eh:')
                print(f'{areaCilindro(raio, altura):.2f}')

            elif status == 'C' and opc_calculo == 'v':
                raio = float(input())
                altura = float(input())
                
                print(f'O volume do cilindro de raio {raio:.2f} e altura {altura:.2f} eh:')
                print(f'{volumeCilindro(raio, altura):.2f}')
            
            elif status == 'E' and opc_calculo == 'a':
                raio = float(input())

                print(f'A area da esfera de raio {raio:.2f} eh:')
                print(f'{areaEsfera(raio):.2f}')

            elif status == 'E' and opc_calculo == 'v':
                raio = float(input())

                print(f'O volume da esfera de raio {raio:.2f} eh:')
                print(f'{volumeEsfera(raio):.2f}')
                
            else:
                print(status)
        else:
            print("Entrada invalida! Entre com 'a' (area) ou 'v' (volume).")
    else:
        print("Entrada invalida! Voce deve usar 'c' (cilindro) ou 'e' (esfera).")