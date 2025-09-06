# Escreva um programa que calcule a quantidade máxima de dados a ser transmitida por um usuário levando em consideração a taxa de transmissão maxima de vídeo, áudio e dados e a capacidade do canal contratado:
# QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade
# O valor de saída deve ser arredondado usando 2 casas decimais

def quantdados(v, a, d, c):
    qdmax = (5.2*v + 3.4*a + 1.5*d) / c
    
    return f'{qdmax:.2f}'

tvideo= float(input()) 
taudio = float(input())
tdados = float(input())
capacidade = float(input())

print(quantdados(tvideo, taudio, tdados, capacidade))

