# O objetivo dessa tarefa é aprender a manipular listas em Python. Deve-se apresentar um programa que leia até 5 notas de um determinado aluno e as guarde em uma lista.
# Em seguida, o programa deve exibir cada nota lida indicando sua posição na lista.

n = int(input())

if n > 0:
    notas_cadastradas = []

    for a in range(n):
        nota = float(input())
        notas_cadastradas.append(nota)
        
    for posicao in range(len(notas_cadastradas)):
        print(f'Nota {posicao+1}: {notas_cadastradas[posicao]}')

    print(f'Media: {sum(notas_cadastradas)/(len(notas_cadastradas)):.2f}')
    
else:
    print('Numero de notas invalido.')