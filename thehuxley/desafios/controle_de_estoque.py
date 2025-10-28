# ler o estoque inicial (máximo de 100 mercadorias)
# leia dos pedidos dos clientes: número do cliente, código da mercadoria, quantidade desejada
# verificar cada pedido, atendido integralmente: 'OK', senão 'ESTOQUE INSUFICIENTE'
# imprimir, no final da execução, o estoque final

# n, m = n: código, m: quant em estoque
# n = 9999, break

# i, j, k: i: código do cliente, j é o código da mercadoria, k : quatnidade solicitada
# i = 9999; break


mercadorias = []
# cadastro de mercadorias:
while True:
    dados_mercadoria = str(input()).split()
    n = int(dados_mercadoria[0])
    if n == 9999:
        break
    
    m = int(dados_mercadoria[1])
    mercadorias.append({"id": n, "quant": m})
    
# print(mercadorias)
    
# cadastro de clientes:
while True:
    dados_clientes = str(input()).split()
    i = int(dados_clientes[0]) # id do cliente
    
    if i == 9999:
        break
    
    j = int(dados_clientes[1]) # id do produto
    k = int(dados_clientes[2]) # quantidade
    
    for i in range(len(mercadorias)):
        if mercadorias[i]['id'] == j:
            item_cadastrado = True
            posicao = i
            # print(mercadorias[i]['quant'])
            
            if mercadorias[i]['quant'] >= k:
                print('OK')
                mercadorias[i]['quant'] = mercadorias[i]['quant'] - k
            else:
                print('ESTOQUE INSUFICIENTE')
            
for registros in mercadorias:
    print(f"{registros['id']} {registros['quant']}")