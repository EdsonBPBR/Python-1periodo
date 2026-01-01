class Produto:
    def __init__(self, nome, marca, preco, validade):
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.validade = validade
        
    def __str__(self):
        return f'{self.nome} - {self.marca} | R$ {self.preco} | {self.validade}'
        