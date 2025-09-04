# Seu objetivo é determinar o maior múltiplo de um inteiro dado menor do que ou igual a um outro inteiro dado

numero = int(input())
numero_limite = int(input())

c = 0
maior = 0
while True:
    c += 1
    multiplo = c * numero
    
    if multiplo > numero_limite:
        break
    else:
        maior = multiplo
    
if maior == 0:
    print(f'sem multiplos menores que {numero_limite}')
else:
    print(maior)