temperatura = float(input('Informe a temperatura: ')) #entre 35 e 41
estado = input("Estado: ") #OU S OU N

#sem considerar decisão para a variável temperatura

if temperatura >= 37 and estado.upper() == "S":
    print('Exames Especiais')

elif temperatura >= 37 and estado.upper() == "N":
    print('Exames Basicos')

elif temperatura < 37 and estado.upper() == "N":
    print('Liberado')

elif temperatura < 37 and estado.upper() == "S":
    print('Exames Basicos')

else:
    print('Erro')