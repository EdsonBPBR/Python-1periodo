# O programa deve identificar os alunos que se destacam, ou seja aqueles cuja média está acima da média da turma, está matriculado e a quantidade de faltas é inferior a 10% da quantidade total da turma.
registros = []
n = int(input())
somatorio_medias = 0
quant_faltas = 0
for i in range(n):
    entrada = str(input()).split()
    matricula = int(entrada[0])
    nome = str(entrada[1])
    sobrenome = str(entrada[2])
    media = float(entrada[3])
    faltas = int(entrada[4])
    status = str(entrada[5])
    
    registros.append({
        "matricula":matricula,
        "nome": nome,
        "sobrenome": sobrenome,
        "media": media,
        "faltas": faltas,
        "status": status
    })
    somatorio_medias += media
    quant_faltas += faltas

media = somatorio_medias/n
vazio = True
for posicao, dado in enumerate(registros):
    if dado['media'] > media and dado['status'] == 'M' and dado['faltas'] < quant_faltas/n:
        print(f"{posicao}:{dado['sobrenome']}")
        vazio = False     
if vazio:
    print('VAZIO')