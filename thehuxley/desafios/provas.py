#  primeiro conjunto de dados a ser lido é o gabarito para a correção da prova. 
gabarito = input().strip().upper()
total_corrigidos = 0
n_aprovados = 0
notas = []

while True:
    nota = 0
    entrada = input().split() 
    
    id = entrada[0]
    if id == '9999':
        break
    # numero, eu quis representar por id, 
    gabarito_aluno = entrada[1].upper()

    # calcular nota com base no gabarito: 
    for i in range(10): # 0 a 9
        if gabarito[i] == gabarito_aluno[i]:
            nota += 1

    if nota >= 6:
        n_aprovados += 1
    
    # exibir a saida formatada:
    print(f'{id} {nota:.1f}')
    notas.append(nota)
    total_corrigidos += 1
        
porcentagem = (100 * n_aprovados) / total_corrigidos
print(f'{porcentagem:.1f}%')

for posicao in range(len(notas)):
    if posicao == 0:
        maior_freq_nota = notas.count(notas[posicao])
        maior_elemento_posi = posicao
    else:
        if notas.count(notas[posicao]) > maior_freq_nota:
            maior_freq_nota = notas.count(notas[posicao])
            maior_elemento_posi = posicao
            
print(f'{notas[maior_elemento_posi]:.1f}')