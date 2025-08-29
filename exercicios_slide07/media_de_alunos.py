# (M ́edia de alunos) Crie um programa em Python para calcular a m ́edia de duas
# notas um conjunto de alunos. Caso o valor -1 seja informado o programa deve
# finalizar sua execu ̧c ̃ao

c = 1
while True:
    n1 = float(input(f'Informe a nota AB1 do aluno {c}: '))
    n2 = float(input(f'Informe a nota AB2 do aluno {c}: '))

    if (n1 == -1) or (n2 == -1):
        print('Script encerrado!')
        break

    media = (n1 + n2) / 2
    print(f'A média do aluno {c} é {media}')

    c += 1