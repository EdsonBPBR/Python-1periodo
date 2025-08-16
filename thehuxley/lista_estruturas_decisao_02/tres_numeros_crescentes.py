# Faça um programa que leia 3 números inteiros e os imprima em ordem crescente.
from random import randint

# numero1 = int(input("Informe o 1º número: "))
# numero2 = int(input("Informe o 2º número: "))
# numero3 = int(input("Informe o 3º número: "))

numero1 = randint(1,5)
numero2 = randint(1,5)
numero3 = randint(1,5)

print(numero1)
print(numero2)
print(numero3)


if (numero1 > numero2 and numero1 > numero3) and (numero2 > numero3):
    print(numero1, numero2, numero3)

elif (numero1 > numero2 and numero1 > numero3) and (numero3 > numero2):
    print(numero1, numero3, numero2)
    
elif (numero2 > numero1 and numero2 > numero3) and (numero1 > numero3):
    print(numero2, numero1, numero3)

elif (numero2 > numero1 and numero2 > numero3) and (numero3 > numero1):
    print(numero2, numero3, numero1)

elif (numero3 > numero1 and numero3 > numero2) and (numero1 > numero2):
    print(numero3, numero1, numero2)

elif (numero3 > numero1 and numero3 > numero2) and (numero2 > numero1):
    print(numero3, numero2, numero1)
    
elif numero1 == numero2 > numero3:
    print(numero1, numero2, numero3)
    
elif numero1 == numero3 > numero2:
    print(numero1, numero3, numero2)
  
elif numero2 == numero3 > numero1:
    print(numero2, numero3, numero1)

elif numero2 == numero1 > numero3:
    print(numero1, numero2, numero3)

else:
    print('TÁ FALTANDO ALGO Q ESQUECI')
#no caso em um nos números for igual