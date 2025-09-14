# Escreva um programa que leia um inteiro que representa a quantidade N de alunos de uma turma. Em seguida, deve ler a matrícula, o nome e a nota de cada um dos alunos. Depois de ler os dados dos N alunos, o programa deve calcular a média das notas dos alunos, imprimir os alunos que têm nota abaixo da média de todos os alunos, seguido dos alunos que têm nota igual ou maior que a média, ordenados de forma crescente pela nota. No final também deve ser impressa a média de todos os alunos.
n = int(input())
registro = []
acima_media = []
abaixo_media = []

somatorio_notas = 0
for _ in range(n):
    entrada = str(input()).split('-')

    matricula = entrada[0]
    nome_aluno = entrada[1]
    nota = float(entrada[2])

    registro.append(f'{nota} {matricula} {nome_aluno}')
    somatorio_notas += nota

media = somatorio_notas / n
print(media)

# processo de decisão
print(registro)

c = 0
while c < n:
    acesso = registro[c]
    nota_individual = float(acesso[0:3])
    if nota_individual >= media:
        acima_media.append(acesso)
    else:
        abaixo_media.append(acesso)
    c += 1

print(acima_media)
print(abaixo_media)
# ainda falta fazer o restante