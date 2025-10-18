#nome, valor mercado, quant grandes jogadores, quant titulo, tem neyvar, flamengo 2019

# valor mecado: pontos
# 1 grande jogador = 100 pontos
# 1 titulo = 1000 pontos
# Se Neymar: 10.000 pontos
# Se flagment: 20.000 pontos

n = int(input())
registros = []

for i in range(n):
    nome = str(input())
    entrada = str(input()).split()
    valor_mercado = float(entrada[0])
    quant_jogadores = int(entrada[1])
    quant_titulos = int(entrada[2])
    
    neymar = str(input()).strip()
    flamengo = str(input()).strip()
    
    if neymar.upper() == 'SIM':
        pontos_neymar = 10000
    else:
        pontos_neymar = 0
        
    if flamengo.upper() == 'SIM':
        pontos_fla = 20000
    else:
        pontos_fla = 0
        
    total_pontos = valor_mercado + (quant_jogadores * 100) + (quant_titulos * 2000) + pontos_neymar + pontos_fla
    
    registros.append([total_pontos, nome])

registros.sort(reverse=True)
for elementos in registros:
    print(f'{elementos[1]} {elementos[0]:.2f}')