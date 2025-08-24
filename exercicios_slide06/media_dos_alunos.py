# 7 (M ́edia de alunos) Crie um programa em Python para calcular a m ́edia de duas
# notas para cinco alunos, para duas notas fornecidas

#range(inicio, limite, incremento)

for k in range(1,6):
    n1 = float(input(f'N1-aluno {k}: '))
    n2 = float(input(f'N2-aluno {k}: '))

    media = (n1 + n2) / 2
    print(f'Média do aluno {k} é {media:.2f}')