programacao_i = []
programacao_ii = []
n = 10

# programacao I:
for i in range(n): # será 45
    matricula_i = int(input())
    programacao_i.append(matricula_i)

# programacao II:
for i in range(5): # será 30 matrículas
    matricula_ii = int(input())
    programacao_ii.append(matricula_ii)
    
alunos_matriculados = programacao_i + programacao_ii
for i in range(len(alunos_matriculados)):
    print(alunos_matriculados.count(alunos_matriculados[i])) # parei aqui, deu mais ou menos certo, só que ele está contabilizando tbm os outros elementos da união, gerando redundância.
    