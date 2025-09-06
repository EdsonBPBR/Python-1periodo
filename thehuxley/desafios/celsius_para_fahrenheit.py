# Escreva um algoritmo para ler uma temperatura dada na escala  Celsius (C) e exibir o equivalente em Fahrenheit (F). Dica: C/5 = (F-32)/9

def celsiusparafarenheint(celsius = 0):
    f = 1.8 * celsius + 32
    return f

temperatura = int(input())
print(f'{celsiusparafarenheint(temperatura):.1f}')