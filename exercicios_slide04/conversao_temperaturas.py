# fahren = float(input('Temperatura em Fahrenheit: '))
# #C / 5 = ( F - 32 ) / 9
# cel = (5 * fahren - 160)/9
# print(f'{fahren} equivale a {cel:.2f}°')

#utilizando funções:
def FahCelsius(temperatura):
    cel = (5 * temperatura - 160)/9
    return cel

def CelsiusFah(temperatura):
    fahren = (9 * temperatura + 160)/5
    return fahren

