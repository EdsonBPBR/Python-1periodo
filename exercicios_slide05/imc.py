# ( ́Indice de Massa Corp ́orea) Crie um programa que calcule o IMC (IMC = P/A*A,
# onde P  ́e o peso e A  ́e a altura.) de uma pessoa e classifique a pessoa de acordo
# com seu IMC:
# IMC abaixo de 17, a sa ́ıda deve ser: ’muito abaixo do peso’;
# IMC entre 17 e 18,49, a sa ́ıda deve ser: ’abaixo do peso’;
# IMC entre 18,5 e 24,99, a sa ́ıda deve ser: ’peso normal’;
# IMC entre 25 e 29,99, a sa ́ıda deve ser: ’acima do peso’;
# IMC entre 30 e 34,99, a sa ́ıda deve ser: ’obsidade’;
# IMC entre 35 e 39,99, a sa ́ıda deve ser: ’obsidade severa’;
# IMC a partir de 40, a sa ́ıda deve ser: ’obesidade morbida’

p = float(input("Informe seu Peso (KG): "))
a = float(input("Informe sua Altura (m): "))

imc = p/(a**2)
print(imc)
print(type(imc))