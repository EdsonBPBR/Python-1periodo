# Consiste de um inteiro n, representando o número de produtos a serem cadastrados. # Depois, segue o cadastro dos n produtos, onde serão lidos para cada produto:# um inteiro representando o código de LED,
# uma descrição do produto
# e um número real representando o preço.
# Depois, são lidos os pedidos.
# O pedido consiste do código do produto e da quantidade de itens daquele produto que será pedido. O pedido se encerra quando o código lido é igual a 0.

n = int(input())
produtos_cadastrados = {}

# cadastrar os produtos
for a in range(n):
    cod = str(input())
    descricao = str(input())
    preco = float(input())
    
    produtos_cadastrados[cod] = [descricao, preco]
    
# pedidos

# print(produtos_cadastrados)
valor_total = 0
while True:
    cod_produto = str(input())
    
    if cod_produto == "0":
        break
    
    quant = int(input())
    
    if cod_produto in produtos_cadastrados and quant > 0:
        valor_total += produtos_cadastrados[cod_produto][1] * quant
    else:
        continue
        
print(f'{valor_total:.2f}')