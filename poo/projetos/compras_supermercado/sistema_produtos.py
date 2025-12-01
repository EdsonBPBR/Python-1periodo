from models import extrairDados, salvarDados

class SistemaProdutos:
    def __init__(self):
        self.lista_produtos = extrairDados()

    def inserir_produto(self, produto):
        self.lista_produtos.append({
            "codigo": produto.codigo,
            "nome": produto.nome,
            "valor": produto.valor,
            "quantidade": produto.quantidade,
            "total": produto.total})
        salvarDados(self.lista_produtos)
        
    def listar_produtos_cadastrados(self):
        return self.lista_produtos

    def remover_produto(self, codigo):
        for i, registro in enumerate(self.lista_produtos):
            if registro['codigo'] == codigo:
                del self.lista_produtos[i]
                salvarDados(self.lista_produtos)
                return True
        return False
    
    def calculo_total(self):
        somatorio_total = 0
        for registro in self.lista_produtos:
            somatorio_total += registro['total']
        return somatorio_total
    
    def busca_codigo(self, codigo):
        for registro in self.lista_produtos:
            if registro['codigo'] == codigo:
                return False
        return True