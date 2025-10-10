# Marcos é um professor bem curioso. Ele gostaria de saber qual é a média de alunos por turma dada a quantidade de turmas, sabendo que cada turma não pode ter mais do que 40 alunos. Faça um programa que peça a quantidade de turmas e a quantidade de alunos em cada turma e mostre a média de alunos por turma.

n = int(input())
somatorio = 0
c = 0

for _ in range(n):
    n_alunos = int(input())
    
    while n_alunos > 40:
        print('O numero de alunos nao pode ser maior que 40')
        n_alunos = int(input())
    else:
        c += 1
        somatorio += n_alunos

print(f'{int(somatorio/c)}')