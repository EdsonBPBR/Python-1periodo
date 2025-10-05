# Uma sequência de 37 pares de inteiros, indicando o número do voo e a quantidade de lugares disponíveis no respectivo voo.
# Cada pedido de reserva é representado por um par de inteiros indicando, respectivamente, o número do documento de identidade do cliente e o número do voo que o cliente deseja viajar. 
voos = {}

for _ in range(37):
    dados = str(input()).split()
    n_voo = str(dados[0])
    quant_lugadores = int(dados[1])
    
    voos[n_voo] = quant_lugadores

while True:
    entrada = str(input()).split()
    n_documento = entrada[0]
    
    if n_documento == "9999":
        break
    
    escolha_voo = entrada[1]
    
    if (escolha_voo in voos) and voos[escolha_voo] >= 1:
        print(n_documento)
        voos[escolha_voo] = voos[escolha_voo] - 1
    else:
        print('INDISPONIVEL')