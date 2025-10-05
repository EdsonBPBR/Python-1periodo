# Leia uma string e imprima somente a última palavra da mesma. Exemplo: Se a string digitada for "José da Silva", deverá ser impresso na tela a substring "Silva".

nome = str(input()).split()
print(nome[-1])
