# A primeira linha contém dois inteiros N e K separados por um espaço em branco (1 <= K <= N <= 100). Cada uma das N linhas seguintes contém uma cadeia de caracteres de tamanho mínimo 1 e máximo 20 representando os nomes dos alunos. Os nomes são compostos apenas por letras minúsculas de 'a' a 'z'.

dados = str(input()).split()
n_alunos = int(dados[0])
n_sorteado = int(dados[1])

alunos_registrados = []

c = 0
while c < n_alunos:
    aluno = str(input())
    alunos_registrados.append(aluno)
    
    c += 1
    
alunos_registrados.sort()
print(alunos_registrados[n_sorteado-1])
    