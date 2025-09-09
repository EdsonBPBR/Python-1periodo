# Rafinha sabe que em sua cidade o valor da KWh de energia varia da forma mostrada abaixo.
#     Até 99 KWh: R$1.35
#     100 até 299 KWh: R$1.55
#     300 até 574 KWh: R$1.75
#     Maior ou igual a 575 KWh: R$2.15

def contaEnergia(energia,):
    if energia <= 99:
        valor = energia * 1.35
        preco_kwh = 1.35

    elif energia >= 100 and energia <= 299:
        valor = energia * 1.55
        preco_kwh = 1.55
        
    elif energia >= 300 and energia <= 574:
        valor = energia * 1.75 * 1.1
        preco_kwh = 1.75 
        
    elif energia >= 575:
        valor = energia * 2.15 * 1.1
        preco_kwh = 2.15

    else:
        print('valor de entrada inválido')
        
    if valor < 35:
        valor = 35
        print(f'{valor:.2f}')
        print(f'{preco_kwh}')
    else:
        print(f'{valor:.2f}')
        print(f'{preco_kwh}')
        
if __name__ == '__main__':
    energia = int(input())
    contaEnergia(energia)