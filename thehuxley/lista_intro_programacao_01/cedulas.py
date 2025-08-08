# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
#células notas: 100, 50, 20, 10, 5, 2 e 1

valor = int(input("Informe o valor: "))

cem = valor // 2 #divisão inteira, número de notas
resto_cem = valor % 100 #resto da divisão por celulas


