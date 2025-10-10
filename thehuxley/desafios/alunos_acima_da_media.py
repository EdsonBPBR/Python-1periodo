# Escreva um programa que leia um inteiro que representa a quantidade N de alunos de uma turma
# em seguida, deve ler a matrícula, nome e nota

n = int(input())
registros = {}
somatorio = 0

for _ in range(n):
    matricula = int(input())
    nome = str(input())
    nota = float(input())
    somatorio += nota
    registros[matricula] = [nota, nome]

media = (somatorio / n)     

resultado = []

for elemento in (registros.keys()):
    if registros[elemento][0] > media:
        x = (registros[elemento][0], elemento, registros[elemento][1])
        resultado.append(x)
    
resultado.sort(reverse=True)

for a in range(len(resultado)):
    if resultado[a][0] == resultado[a-1][0]:
        resultado.sort()

for posicoes in range(len(resultado)):
    print(f'Matricula: {resultado[posicoes][1]} Nome: {resultado[posicoes][2]} Nota: {resultado[posicoes][0]}')

print(f'Media = {media:.2f}')