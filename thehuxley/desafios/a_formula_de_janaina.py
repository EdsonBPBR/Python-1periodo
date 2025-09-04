# Janaína, estudante de Engenharia de Materiais, precisa calcular o resultado de x ao quadrado menos quatro x mais cinco (x**2 - 4*x + 5). Só que ela precisa calcular o resultado dessa fórmula para vários valores de x dentro de um determinado intervalo.
# Dois números inteiros, um em cada linha:
# O primeiro número (a) representa o primeiro valor de x que deve ser utilizado
# O segundo número (b) representa o último valor de x que deve ser utilizado

a = int(input())
b = int(input())

for x in range(a, b+1):
    print(x**2 - 4*x + 5)