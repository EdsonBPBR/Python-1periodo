import json

def extrairDados():
    with open('poo/projetos/compras_supermercado/registros.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def salvarDados(dados_atualizados):
    with open('poo/projetos/compras_supermercado/registros.json', 'w') as arquivo:
        json.dump(dados_atualizados, arquivo, indent=4, ensure_ascii=False)
       
# dados_usuarios = extrairDados()       
# dados_usuarios.append({
#             "codigo": 123,
#             "valor": 15.2,
#             "quantidade": 10,
#             "total": 152})
# salvarDados(dados_usuarios)