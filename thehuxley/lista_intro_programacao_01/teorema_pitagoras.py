# Faça um programa que calcule o valor da hipotenusa de acordo com o teorema de pitágoras. Você não precisa se preocupar com casos em que os catetos fornecidos não podem formar um triângulo.
# Pesquise como fazer a operação de raiz quadrada.
# O valor de saída deve ser arredondado usando 2 casas decimais.

cateto_ad = float(input("Informe o valor do cateto adjacente: "))
cateto_op = float(input("Informe o valor do cateto oposto: "))

h = cateto_ad ** 2 + cateto_op ** 2
print(f'{h**(1/2):.2f}')