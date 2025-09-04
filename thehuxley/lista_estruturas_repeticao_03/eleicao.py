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
n_votos_validos = 0

votos_totais_a = 0
votos_totais_b = 0
votos_totais_c = 0
votos_totais_brancos = 0
votos_totais_nulos = 0

c = 0
while True:
    sessao = int(input())
    if sessao == 0:
        break
    
    votos_a = int(input())
    votos_b = int(input())
    votos_c = int(input())
    votos_brancos = int(input())
    votos_nulos = int(input())
    
    n_votantes += (votos_a + votos_b + votos_c + votos_brancos + votos_nulos)
    n_votos_validos += (votos_a + votos_b + votos_c)
    
    votos_totais_a += votos_a
    votos_totais_b += votos_b    
    votos_totais_c += votos_c
    votos_totais_brancos += votos_brancos
    votos_totais_nulos += votos_nulos
        
    c += 1

print(f'Numero de votantes: {n_votantes}')
print(f'Total A: {votos_totais_a}')
print(f'Total B: {votos_totais_b}')
print(f'Total C: {votos_totais_c}')
print(f'Brancos: {votos_totais_brancos}')
print(f'Nulos: {votos_totais_nulos}')
print(f'Validos: {n_votos_validos}')

if votos_totais_a > votos_totais_b and votos_totais_a > votos_totais_c:
    if votos_totais_a >= (1/2 * n_votos_validos):
        segundo_turno = False
    else:
        segundo_turno = True
    
    print('Candidato mais votado: A')
elif votos_totais_b > votos_totais_a and votos_totais_b > votos_totais_c:
    if  votos_totais_b >= (1/2 * n_votos_validos):
        segundo_turno = False
    else:
        segundo_turno = True
    
    print('Candidato mais votado: B')
elif votos_totais_c > votos_totais_a and votos_totais_c > votos_totais_b:
    if  votos_totais_c >= (1/2 * n_votos_validos):
        segundo_turno = False
    else:
        segundo_turno = True
        
    print('Candidato mais votado: C')
    
elif votos_totais_a == votos_totais_b == votos_totais_c == 0:
    print('Candidato mais votado: ')
    segundo_turno = False
    
else:
    print('Candidato mais votado: ')
    segundo_turno = True
    
if (votos_totais_brancos + votos_totais_nulos) < n_votos_validos:
    print('Eleicao valida? True')
else:
    print('Eleicao valida? False')

print(f'Segundo turno? {segundo_turno}')