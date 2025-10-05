#  Nessas eleições concorrem os candidatos 83-Alibabá e 93-Alcapone. Cada voto deve ser dado pelo número do candidato, permitindo-se ainda o voto 0 para voto em branco. Qualquer voto diferente dos já citados é considerado nulo.

n_alibaba = 0
n_alcapone = 0
nulos = 0
branco = 0
votos_validos = 0

while True:
    voto = int(input())
    
    if voto == -1:
        break
    
    if voto == 83:
        n_alibaba += 1
        votos_validos += 1
    elif voto == 93:
        n_alcapone += 1
        votos_validos += 1
    elif voto == 0:
        branco += 1
        votos_validos += 1
    else:
        nulos += 1

if n_alcapone > n_alibaba:
    ganhador = 93
else:
    ganhador = 83

porcentagem_a = (100 * n_alibaba) / votos_validos
porcentagem_b = (100 * n_alcapone) / votos_validos

print(n_alibaba)
print(n_alcapone)
print(branco)
print(nulos)
print(ganhador)
print(f'{porcentagem_a:.2f}')
print(f'{porcentagem_b:.2f}')

