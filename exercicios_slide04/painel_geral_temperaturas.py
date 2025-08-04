from conversao_temperaturas import FahCelsius, CelsiusFah

if __name__ == "__main__":
    print('[1] - FAHRENHEIT PARA CELSIUS')
    print('[2] - CELSIUS PARA FAHRENHEIT')

    opcao = int(input('Informe a opção:'))
    print('---'*10)

    if opcao == 1:
        temperatura = float(input('FAHRENHEIT PARA CELSIUS:'))
        print(f'{FahCelsius(temperatura)}°')
    
    elif opcao == 2:
        temperatura = float(input('CELSIUS PARA FAHRENHEIT: '))
        print(f'{CelsiusFah(temperatura)}°')

    else:
        print('Opção INVÁLIDA!')