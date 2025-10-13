# Escreva um programa que leia um inteiro que representa a quantidade N de alunos de uma turma
# em seguida, deve ler a matrícula, nome e nota

n = int(input())
registros = []
somatorio = 0

for _ in range(n):
    matricula = int(input())
    nome = str(input())
    nota = float(input())
    somatorio += nota
    registros.append((matricula, nota, nome))

media = (somatorio / n)     
registros.sort(reverse=True) # ordenar por matricula

resultado = []
for a in range(len(registros)):
    resultado.append((registros[a][1], registros[a][0], registros[a][2]))
                        # matricula         nota         nome  
 
resultado.sort()

for i in range(len(resultado)):
    if resultado[i][0] > media:
        print(f'Matricula: {resultado[i][1]} Nome: {resultado[i][2]} Nota: {resultado[i][0]}')

print(f'Media = {media:.2f}')