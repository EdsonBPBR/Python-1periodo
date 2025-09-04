# Para realizar a totalização dos votos de uma eleição para um cargo majoritário com 3 candidatos, leia os votos de cada seção até seja digitado o número da secção seja 0 (zero). Para cada secção são informados: o número de votos do candidato A, B, C, o número de
# votos brancos e nulos. Então determine:
# a. O número de votantes
# b. O total de votos de cada candidato
# c. O total de votos brancos e de votos nulos
# d. O total de votos válidos
# e. O candidato com maior votação
# f. Se a eleição foi válida e para isso o total de votos brancos mais votos nulos deve ser menor que o total de votos válidos
# g. Se haverá segundo turno, para não haver segundo turno basta que o total de votos do candidato vencedor seja maior que 50% dos votos válidos

n_votantes = 0
while True:
    voto = int(input())
    n_votantes += voto
    
    if voto == 0:
        break

print(f'Numero de votantes: {n_votantes}')